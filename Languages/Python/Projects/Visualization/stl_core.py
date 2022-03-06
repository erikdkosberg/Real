import numpy as np
from stl import mesh

vertices = np.array([
    [0,0,4], #0
    [0,1,1], #1
    [1,1,1], #2
    [1,0,1], #3
    [0,0,0], #4
    [0,1,0], #5 
    [1,1,0], #6
    [1,0,0], #7
    [3,3,0], #8
    [3,2,0], #9
    [0,1,-3], #10
    [3,3,-3], #11
    [4,2,0], #12
    [0,0,-2], #13
    [1,0,-2], #14
    [0,0,-3], #15
    [3,2,-3], #16
    [3,2,-2], #17
    [4,2,-2], #18
])

faces = np.array([
    [0,2,1],
    [0,3,2],
    
    [0,1,5],
    [0,5,4],
    
    [5,1,2],
    [5,2,6],
    
    [3,6,2],
    [3,7,6],
    
    [0,4,7],
    [0,7,3],
    
    [6,8,5],
    [6,9,8],
    
    [5,8,11],
    [5,11,10],
    
    [6,7,12],
    [6,12,9],
    
    [4,13,14],
    [4,14,7],
    
    [4,10,15],
    [4,5,10],
    
    [8,16,11],
    [8,9,16],
    
    [9,12,18],
    [9,18,17],
    
    [7,18,12],
    [7,14,18],
    
    [13,17,18],
    [13,18,14],
    
    [13,15,16],
    [13,16,17],
    
    [15,10,11],
    [15,11,16],
])

shape = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        shape.vectors[i][j] = vertices[f[j], :]

shape.save("parallelepipeds.stl")

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure, auto_add_to_figure=False)

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file("parallelepipeds.stl")
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

figure.add_axes(axes)

# Show the plot to the screen
pyplot.show()