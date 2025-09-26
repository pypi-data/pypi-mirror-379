import os
import re
import trimesh
import numpy as np
import os.path as osp
from typing import List, Dict

from libpsc import *


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def extract_fn(query, pattern):
    return re.search(pattern, query).groups()


def to_list_of_type_fn(t, lst):
    return list(map(t, lst))


SPACE = r"\s+"
PART = rf"{SPACE}(\S+)"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def write_psc(
    filepath: str,
    op_lst: List[Dict],
    pt: List[float] = [0.0, 0.0, 0.0],
) -> None:
    """write out a psc file for saving a progressive simplicial complex representation

    Params:
        filepath: str
            the output file path to write the psc file
        op_lst: List[Dict]
            a list of vertex split operations
            each operation is a dictionary containing:
            - "vsid": int, >=0, source vertex index
            - "vtid": int, >=0, target vertex index
            - "code": str, topology list
            - "position_bit": int, splitting mode, 0 == midpoint == also update vs
            - "delta_p": List[float] of length 3, relative translation vector
        pt: List[float] of length 3
            the starting point location
    """
    # make sure directory exists
    os.makedirs(osp.dirname(filepath), exist_ok=True)

    # write the file content
    with open(filepath, "w") as f:
        # write the header
        f.write(
            '[Attributes]\nmat="black" groups="XXX" rgb=(1 0 0) norgroup=1 attrid=0\n'
        )
        f.write("[EndAttributes]\n")

        # write the initial simplex (assumed to be a single vertex)
        f.write(f"Simplex 0 1 {pt[0]} {pt[1]} {pt[2]}\n")
        f.write("#\n")

        # write each operation in the operation list
        for op in op_lst:
            delta_p = op["delta_p"]
            assert len(delta_p) == 3, "delta_p must be a list of 3 floats."

            vsid = int(op["vsid"])
            vtid = int(op["vtid"])
            code = str(op["code"])
            position_bit = int(op["position_bit"])
            delta_p = [float(x) for x in delta_p]

            # write one operation
            f.write(f"{vsid + 1} {vtid + 1}\n")  # >= 1
            f.write(f"{code}\n")
            f.write(f"{position_bit} {delta_p[0]} {delta_p[1]} {delta_p[2]}\n")
            f.write("-1\n-1\n")

    print(f"saved psc file to: {filepath}")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def load_psc(file_path: str):
    """load psc file"""
    out = dict(
        center=[0, 0, 0],  # the starting point location
        vsplits=[],  # the operation sequence to split vertex
    )

    with open(file_path, "r") as f:
        lines_all = f.readlines()

    idx_line, simplex_loaded = 0, False
    while idx_line < len(lines_all):
        line = lines_all[idx_line].strip()

        if any(line.startswith(c) for c in ("#", "[", "m")):  # not important line
            idx_line += 1

        elif line.startswith("Simplex"):  # starting point location
            out["center"] = to_list_of_type_fn(
                float,
                extract_fn(line, rf"Simplex{SPACE}\S+{SPACE}\S+{PART}{PART}{PART}"),
            )
            simplex_loaded = True
            idx_line += 1

        elif simplex_loaded:  # load one vsplit info
            # vertex id: source, target
            vsid, vtid = to_list_of_type_fn(
                int, extract_fn(lines_all[idx_line + 0].strip(), rf"(\S+){PART}")
            )

            # a string code
            code = lines_all[idx_line + 1].strip()

            # position bit: (see "SplitRecord::applySplit")
            #   always set "vt" as "vs_p + delta_p"
            #   0 ==> midpoint ==> also set "vs_p" as "vs_p - delta_p"
            #   1 ==>          ==> keep     "vs_p" unchanged
            # position offset
            position_bit, *delta_p = to_list_of_type_fn(
                float,
                extract_fn(
                    lines_all[idx_line + 2].strip(), rf"(\S+){PART}{PART}{PART}"
                ),
            )
            position_bit = int(position_bit)

            # wait until meeting two "-1"
            offset, cnt_neg1 = 0, 0
            while cnt_neg1 < 2:
                line = lines_all[idx_line + 3 + offset].strip()
                if line == "-1":
                    cnt_neg1 += 1
                offset += 1

            # save results
            out["vsplits"].append(
                dict(
                    vsid=vsid - 1,  # >= 0
                    vtid=vtid - 1,  # >= 0
                    code=code,
                    position_bit=position_bit,
                    delta_p=delta_p,
                )
            )

            idx_line += 3 + offset

    return out


def load_sc(file_path: str):
    """load sc file
    Returns:
        pack (list of ndarray):
            dim ==> ndarray
             0  ==> vertex coordinates
             1  ==> edges: relative to points
             2  ==> faces: relative to points
    """
    pack = [[], [], []]

    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("Simplex 0"):
                pack[0].append(
                    to_list_of_type_fn(
                        float,
                        extract_fn(
                            line, rf"Simplex{SPACE}0{SPACE}\S+{PART}{PART}{PART}"
                        ),
                    )
                )
            elif line.startswith("Simplex 1"):
                pack[1].append(
                    to_list_of_type_fn(
                        int, extract_fn(line, rf"Simplex{SPACE}1{SPACE}\S+{PART}{PART}")
                    )
                )
            elif line.startswith("Simplex 2"):
                pack[2].append(
                    to_list_of_type_fn(
                        int,
                        extract_fn(
                            line, rf"Simplex{SPACE}2{SPACE}\S+{PART}{PART}{PART}"
                        ),
                    )
                )

    # NOTE : indices are sorted along the row
    pack[0] = np.asarray(pack[0])
    pack[1] = np.asarray(pack[1]) - 1  # >=0
    pack[2] = np.asarray(pack[2]) - 1  # >=0
    pack[2] = pack_to_faces(pack)  # relative to verts

    return pack


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def pack_to_faces(pack):
    """convert the "line index" to "vert index"
    i.e., triangle mesh's "faces" variable
    """
    if len(pack[2]) == 0:  # no faces
        return np.zeros([0, 3]).astype(np.int64)
    faces = np.asarray(
        [np.unique(f) for f in pack[1][pack[2]].reshape(-1, 6)]
    )  # (num_faces, 3)
    return faces


def compute_taken_mask(pack):
    """compute mask of used vertices/edges"""
    # see if verts have been used by edges/faces
    v_taken = np.unique(
        np.concatenate([pack[1].reshape(-1), pack[2].reshape(-1)], axis=0)
    )
    msk_v = np.isin(np.arange(len(pack[0])), v_taken)

    # see if edges have been used by faces
    msk_e = np.zeros([len(pack[1])], dtype=np.bool)
    if len(pack[2]) >= 1:
        e_taken = np.unique(
            np.concatenate(
                [pack[2][:, [0, 1]], pack[2][:, [1, 2]], pack[2][:, [0, 2]]],
                axis=0,
            ),
            axis=0,
        )
        dtype = [("col1", np.int64), ("col2", np.int64)]
        msk_e = np.isin(
            pack[1].astype(np.int64).view(dtype), e_taken.astype(np.int64).view(dtype)
        ).reshape(-1)

    return msk_v, msk_e


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def export_triangle_mesh(file_path: str, pack):
    """convert the "line index" to "vert index"
    i.e., triangle mesh's "faces" variable
    """
    # this internally removes unreferenced vertices because "process=True" by default
    mesh = trimesh.Trimesh(vertices=pack[0], faces=pack[2])
    mesh.export(file_path)


def export_visual_mesh(file_path: str, pack, radius=0.05, principal=True):
    """export simplicial complex as a mesh for visualization
    (by transforming isolated points as spheres, and isolated edges as cylinders)
    """
    verts, edges, faces = pack

    # only take principal simplices
    msk_v, msk_e = (
        compute_taken_mask(pack)
        if principal
        else [np.zeros(len(pack[i]), dtype=np.bool) for i in range(2)]
    )

    # isolated point
    mesh_v = list()
    sphere_template = trimesh.creation.uv_sphere(radius=radius, count=[5, 3])
    for pt in verts[~msk_v]:
        mesh_v.append(sphere_template.copy().apply_translation(pt))

    # isolated edges
    mesh_e = list()
    for idx1, idx2 in edges[~msk_e]:
        transform, height = trimesh.creation._segment_to_cylinder(
            segment=np.stack([verts[idx1], verts[idx2]])
        )
        mesh_e.append(
            trimesh.creation.capsule(
                radius=radius, transform=transform, height=height, count=[5, 5]
            )
        )

    # surface triangles (this internally removes unreferenced vertices because "process=True" by default)
    mesh_f = trimesh.Trimesh(vertices=verts, faces=faces)

    # export the file
    mesh_vef = trimesh.util.concatenate(mesh_v + mesh_e + [mesh_f])
    mesh_vef.export(file_path)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def export_triangle_mesh_from_psc(file_path: str, psc):
    """export triangle mesh"""
    verts, edges, faces = map(np.asarray, psc.write())
    export_triangle_mesh(file_path, (verts, edges, faces))
    print(f"export triangle mesh to: {file_path}")


def export_visual_mesh_from_psc(file_path: str, psc, radius=0.05, principal=True):
    """export visualizable mesh"""
    verts, edges, faces = map(np.asarray, psc.write())
    export_visual_mesh(
        file_path, (verts, edges, faces), radius=radius, principal=principal
    )
    print(f"export visual mesh to: {file_path}")


def export_npz_from_psc(file_path: str, psc):
    """export npz for simplicial complex"""
    verts, edges, faces = map(np.asarray, psc.write())
    np.savez_compressed(file_path, verts=verts, edges=edges, faces=faces)
    print(f"export npz mesh to: {file_path}")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def find_sharp_and_boundary_edges(
    mesh,
    is_sharp_fn=lambda cos_val: cos_val < np.cos(np.deg2rad(45)),
):
    """find sharp and boundary edges of the given mesh
    Params:
        mesh (Trimesh):
            the trimesh object
        is_sharp_fn (lambda) :
            whether the cosine angle of an edge between two adjacent faces is considered sharp
    """

    # find boundary edges
    num_verts = len(mesh.vertices)
    edges = mesh.edges_unique  # all the edges
    edges_interior = mesh.face_adjacency_edges  # each row is (idx_v0, idx_v1)
    edges_hashed = edges[:, 0] + edges[:, 1] * num_verts
    edges_interior_hashed = edges_interior[:, 0] + edges_interior[:, 1] * num_verts
    is_interior = np.isin(edges_hashed, edges_interior_hashed)
    edges_boundary = edges[~is_interior]

    # find sharp edges
    face_adjacency = mesh.face_adjacency  # each row is (idx_f0, idx_f1)
    face_normals = mesh.face_normals
    assert len(edges_interior) == len(face_adjacency)
    normals_a = face_normals[face_adjacency[:, 0]]
    normals_b = face_normals[face_adjacency[:, 1]]
    cos_val = np.sum(normals_a * normals_b, axis=1)
    msk_sharp = is_sharp_fn(cos_val)
    edges_sharp = edges_interior[msk_sharp]
    cos_val_sharp = cos_val[msk_sharp]

    # output
    return edges_boundary, edges_sharp, cos_val_sharp


def obtain_psc_sequence_from_mesh(
    mesh,
    weightings=[0, 1, 1],
    weighting_topo=1,
    is_sharp_fn=lambda cos_val: cos_val < np.cos(np.deg2rad(45)),
    sharpness_fn=lambda cos_val: (
        (np.cos(np.deg2rad(45)) - cos_val) / (np.cos(np.deg2rad(45)) + 1)
    ).clip(min=0, max=1),
    std_v=1e-5,
    return_cost=False,
):
    """load the mesh and obtain the psc sequence
    Params:
        mesh (str/Trimesh): the input mesh file path, or the Trimesh object
        weightings (list of float):
            the volume weighting of vertices, edges and faces
            setting to <0 will disable further weighting
            setting to =0 will disable the quadrics (zero out)
            setting to >0 will weight the quadrics by the volume and also the positive weighting factor
        weighting_topo (float):
            the penalty factor for topological changes
            a higher value indicates postponing the topological changes during the simplification
            the effect is not very significant
        is_sharp_fn (fn): return True if the edge is considered sharp
        sharpness_fn (fn): return a 0~1 factor with 1 being very sharp, and 0 being non-sharp
        return_cost (bool): whether to return the cost of each operation
    """
    if isinstance(mesh, str):
        mesh = trimesh.load(mesh, process=False)
    mesh.vertices += np.random.RandomState(42).randn(*mesh.vertices.shape) * std_v
    #
    verts, faces = np.asarray(mesh.vertices), np.asarray(mesh.faces)
    edges_boundary, edges_sharp, cos_val_sharp = find_sharp_and_boundary_edges(
        mesh, is_sharp_fn=is_sharp_fn
    )
    w_edges_boundary = np.ones([len(edges_boundary)])
    w_edges_sharp = sharpness_fn(cos_val_sharp)

    weighting_v = [weightings[0] for _ in range(len(verts))]
    weighting_e = (
        (np.concatenate([w_edges_boundary, w_edges_sharp])) * weightings[1]
    ).tolist()
    weighting_f = [weightings[2] for _ in range(len(faces))]

    edges = np.vstack([edges_boundary, edges_sharp])
    psc = PSC(
        verts, edges, faces, weighting_v, weighting_e, weighting_f, weighting_topo
    )

    if return_cost:
        op_lst, cost_lst, pt = psc.simplify_with_cost()
        return op_lst, cost_lst, pt
    
    op_lst, pt = psc.simplify()

    return op_lst, pt


def reconstruct(op_lst, pt=[0.0, 0.0, 0.0], ratio=1.0):
    """reconstruct the scene from the psc sequence
    Params:
        ratio (float) : the percentage ratio of the operations applied to recover
    """
    assert 0 <= ratio <= 1

    psc = PSC(pt)
    for op in op_lst[: round(ratio * len(op_lst))]:
        psc.gvspl(op["vsid"], op["vtid"], op["code"], op["position_bit"], op["delta_p"])

    return psc
