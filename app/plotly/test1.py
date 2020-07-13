import plotly
plotly.__version__
import numpy as np
from stl import mesh
import plotly.graph_objects as go 

# your_mesh = mesh.Mesh.from_file('stl-test.stl')

# VERTICE_COUNT = 100
# data = numpy.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
# your_mesh = mesh.Mesh(data, remove_empty_areas=False)

# your_mesh.normals

# your_mesh.v0, your_mesh.v1, your_mesh.v2
# assert (your_mesh.points[0][0:3] == your_mesh.v0[0]).all()
# assert (your_mesh.points[0][3:6] == your_mesh.v1[0]).all()
# assert (your_mesh.points[0][6:9] == your_mesh.v2[0]).all()
# assert (your_mesh.points[1][0:3] == your_mesh.v0[1]).all()

# your_mesh.save('new_stl_file.stl')

def stl2mesh3d(stl_mesh):
    p, q, r = stl_mesh.vectors.shape
    vertices, ixr = np.unique(stl_mesh.vectors.reshape(p*q, r), return_inverse=True, axis = 0)
    I = np.take(ixr, [3*k for k in range(p)])
    J = np.take(ixr, [3*k+1 for k in range(p)])
    K = np.take(ixr, [3*k+2 for k in range(p)])
    return vertices, I, J, K

my_mesh = mesh.Mesh.from_file('stl-test.stl')
# my_mesh.vectors.shape 
vertices, I, J, K = stl2mesh3d(my_mesh)
x, y, z = vertices.T
# vertices.shape 
colorscale = [[0, '#e5dee5'], [1, 'e5dee5']]

mesh3D = go.Mesh3d(
    x=x,
    y=y,
    z=z,
    i=I,
    j=J,
    k=K,
    flatshading=True,
    colorscale=colorscale,
    intensity=z,
    name='STL-test',
    showscale=False
)


