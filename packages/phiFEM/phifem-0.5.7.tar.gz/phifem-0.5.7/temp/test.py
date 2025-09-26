import dolfinx as dfx
import numpy as np
import ufl
from dolfinx.fem import assemble_scalar
from mpi4py import MPI

mesh = dfx.mesh.create_unit_square(MPI.COMM_WORLD, 5, 5)


def f(x):
    return ufl.sin(x[0])


print(type(f))
x_ufl = ufl.SpatialCoordinate(mesh)

dx = ufl.Measure("dx", domain=mesh)

integral = f(x_ufl) * dx
form = dfx.fem.form(integral)
val = assemble_scalar(form)
print(val)
