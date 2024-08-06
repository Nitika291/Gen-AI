"""Create a base class Shape with an abstract method calculate_area (not implemented).  Create subclasses Square and Circle inheriting from Shape. Implement the calculate_area method in each subclass to calculate the area based on its specific properties (side length for square, radius for circle)."""
from abc import ABC, abstractmethod
import math

# Base class Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


# Subclass Square inheriting from Shape
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2


# Subclass Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


# Example usage
if __name__ == "__main__":
    square = Square(54)
    print(f"Square area: {square.calculate_area()}")

    circle = Circle(43)
    print(f"Circle area: {circle.calculate_area():.2f}")
