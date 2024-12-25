from abc import ABC, abstractmethod

# Product Interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Products
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Factory Class
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "SQUARE":
            return Square()
        elif shape_type == "RECTANGLE":
            return Rectangle()
        else:
            return None

# Client Code
if __name__ == "__main__":
    shape_factory = ShapeFactory()

    shape1 = shape_factory.get_shape("CIRCLE")
    print(shape1.draw())

    shape2 = shape_factory.get_shape("SQUARE")
    print(shape2.draw())

    shape3 = shape_factory.get_shape("RECTANGLE")
    print(shape3.draw())