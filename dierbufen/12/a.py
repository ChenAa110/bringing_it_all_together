import math


class Apple:
    def __init__(self, size, color, name, price):
        self.size = size
        self.color = color
        self.name = name
        self.price = price


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi


circle = Circle(20)
print(circle.area())


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.height * self.base / 2


triangle = Triangle(20,50)
print(triangle.area())



class Hexagon:
    def __init__(self, a, b,c):
        self.a = a
        self.b = b
        self.c = c

    def cacculate_perimeter(self):
        return self.a+self.b+self.c

hexagon=Hexagon(10,10,10)
print(hexagon.cacculate_perimeter())
