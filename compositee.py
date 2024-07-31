'''
The composite pattern is a design pattern that allows for the creation of a hierarchical tree-like structure of objects, where each object in the structure can be either a leaf node (a basic element) or a composite node (a container for other objects). This pattern allows for the treatment of both leaf nodes and composite nodes in the same way, making it easy to add new types of objects to the structure without affecting the existing code.

Here is an example scenario where the composite pattern can be used:

Let's say you are building a graphic design tool that allows users to create and edit complex shapes. The shapes can be basic elements such as circles and rectangles, or they can be composed of other shapes. The tool should allow users to manipulate the shapes as if they were single objects, regardless of whether they are basic elements or composite shapes.

Here's an example code that illustrates how the composite pattern can be used to implement this scenario:
'''
class Shape:
    def draw(self):
        pass

class CompositeShape(Shape):
    def __init__(self):
        self.shapes = []

    def draw(self):
        for shape in self.shapes:
            shape.draw()

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        self.shapes.remove(shape)

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

# Creating basic shapes
circle = Circle()
rectangle = Rectangle()

# Creating a composite shape
composite_shape = CompositeShape()
composite_shape.add_shape(circle)
composite_shape.add_shape(rectangle)

# Draw composite shape
composite_shape.draw()
# Output:
# Drawing a Circle
# Drawing a Rectangle
