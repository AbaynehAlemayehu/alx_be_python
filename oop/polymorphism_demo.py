# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method for calculating area - must be overridden in subclasses"""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width"""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * (self.radius ** 2)
