import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())
