"""
So the question is,

is it possible to have a class that helps you create an stl file with some sort of interactive prompt?

Here are the necessary pieces of information to create a shape:


"""

# Faces is a Nx3 array of integers indexing the three vertices of each triangle

class CreateStl:
    def __init__(self, vertices, faces):
        self.name = "STL Library"
        self.vertices = vertices
        self.faces = faces


    def get_coordinates(self):
        return [input(f"Please enter the x,y,z for vertice #{z+1}(sep by ','):    ") for z in range(self.vertices)]

    def main(self):
        pass

test = CreateStl(2,2).get_coordinates()
print(test)