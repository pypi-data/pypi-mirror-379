import dolfinx as dfx
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from basix.ufl import element
from dolfinx.io import XDMFFile
from meshtagsplot import plot_mesh_tags
from mpi4py import MPI

from src.phifem.mesh_scripts import compute_tags_measures

"""
def levelset(x):
    R = 0.47
    size_osc = 2.0
    r = np.sqrt(x[0, :] ** 2 + x[1, :] ** 2)
    theta = np.arctan2(x[1], x[0])
    val = (
        r**4 * (np.full_like(r, 5.0) + size_osc * theta * np.sin((5.0 / theta))) / 2.0
        - R**4
    )
    return val


bbox = np.array([[-0.5, 0.5], [-0.5, 0.5]])
"""


def levelset(x):
    r = np.sqrt(x[0] ** 2 + x[1] ** 2)
    R = 2.0
    radius = 0.5
    theta = np.arctan2(x[1], x[0])

    val = (
        r
        * (
            1.0
            + 0.75
            * np.abs(theta)
            * np.sqrt(
                radius**2
                - (
                    1.0 / (np.sqrt(np.abs(theta)) + 1.0e-18)
                    - np.floor(1.0 / (np.sqrt(np.abs(theta)) + 1.0e-18) + radius)
                )
                ** 2
            )
        )
        - R
    )

    return val


bbox = np.array([[-1.7, 2.2], [-1.5, 1.5]])


x, y = (
    np.linspace(bbox[0, 0], bbox[0, 1], 1000),
    np.linspace(bbox[1, 0], bbox[1, 1], 1000),
)
X, Y = np.meshgrid(x, y)
XY = np.vstack([X, Y])
z = levelset(XY)
print(z)
fig = go.Figure(data=[go.Surface(z=z)])

fig.write_html("levelset.html")

# Create background mesh
initial_mesh_size = 0.05 * np.sqrt(2.0)
box_mode = False
detection_degree = 5
nx = int(np.abs(bbox[0][1] - bbox[0][0]) / initial_mesh_size / np.sqrt(2.0))
ny = int(np.abs(bbox[1][1] - bbox[1][0]) / initial_mesh_size / np.sqrt(2.0))

# cell_type = dfx.cpp.mesh.CellType.triangle
# mesh = dfx.mesh.create_rectangle(
#     MPI.COMM_WORLD, np.asarray(bbox).T, [nx, ny], cell_type
# )

import adios4dolfinx

mesh = adios4dolfinx.read_mesh("checkpoint_02.bp", comm=MPI.COMM_WORLD)
cells_tags, facets_tags, submesh, ds, _, _ = compute_tags_measures(
    mesh, levelset, detection_degree, box_mode=box_mode
)

fig = plt.figure()
ax = fig.subplots()
plot_mesh_tags(submesh, cells_tags, ax, expression_levelset=levelset)
plt.savefig("cells_tags.png", dpi=500)

leg_dict = {1: "in", 2: "cut", 3: "boundary_in", 4: "boundary_out"}
fig = plt.figure()
ax = fig.subplots()
plot_mesh_tags(
    submesh, facets_tags, ax, expression_levelset=levelset, leg_dict=leg_dict
)
plt.savefig("facets_tags.png", dpi=500, bbox_inches="tight")

cell_name = mesh.topology.cell_name()
fe_element = element("Lagrange", cell_name, 1)
fe_space = dfx.fem.functionspace(mesh, fe_element)

phih = dfx.fem.Function(fe_space)
phih.interpolate(levelset)

with XDMFFile(mesh.comm, "levelset.xdmf", "w") as of:
    of.write_mesh(mesh)
    of.write_function(phih)
