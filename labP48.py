#Q48. creating a class that represents a shape and implementing subclasses for different shapes like circle, triangle, and square:

import math

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2
    def perimeter(self): return 2 * math.pi * self.r

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)(s-self.b)(s-self.c))**0.5
    def perimeter(self): return self.a + self.b + self.c

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

# Example
shapes = [Circle(5), Triangle(3, 4, 5), Square(4)]
for s in shapes:
    print(f"{s._class.name_}: Area = {s.area():.2f}, Perimeter = {s.perimeter():.2f}")