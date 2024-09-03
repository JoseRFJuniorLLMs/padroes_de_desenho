"""
Propósito: Define una interfaz para crear un objeto, pero permite a las subclases alterar el tipo de objeto que será creado.
"""

class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        return "Drawing a circle"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a rectangle"

class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Unknown shape type")

# Uso
factory = ShapeFactory()
shape = factory.get_shape("circle")
print(shape.draw())  # Imprime: Drawing a circle
