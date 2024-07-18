from abc import ABC, abstractmethod

# Abstract Factory Interface
class AbstractShapeFactory(ABC):
    @abstractmethod
    def create_circle(self):
        pass

    @abstractmethod
    def create_square(self):
        pass

    @abstractmethod
    def create_rectangle(self):
        pass

# Concrete Factory Class
class ShapeFactory(AbstractShapeFactory):
    def create_circle(self):
        return Circle()

    def create_square(self):
        return Square()

    def create_rectangle(self):
        return Rectangle()

# Shape Classes
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Client Code
if __name__ == "__main__":
    shape_factory = ShapeFactory()

    circle = shape_factory.create_circle()
    print(circle.draw())

    square = shape_factory.create_square()
    print(square.draw())

    rectangle = shape_factory.create_rectangle()
    print(rectangle.draw())