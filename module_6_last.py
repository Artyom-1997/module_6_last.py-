class Fig:


    Sides_count = 0


def __init__(self, sides, color):


    self.__sides = sides
self.__color = color


def get_sides(self):


    return self.__sides


def set_sides(self, sides):


    self.__sides = sides


def get_color(self):


    return self.__color


def set_color(self, color):


    self.__color = color


class Circle(Fig):


    def __init__(self, radius, color):


    super().__init__([radius], color)


def get_radius(self):


    return self.get_sides()[0]


def set_radius(self, radius):


    self.set_sides([radius])


class Triangle(Fig):


    def __init__(self, side1, side2, side3, color):


    super().__init__([side1, side2, side3], color)


def get_side1(self):


    return self.get_sides()[0]


def get_side2(self):


    return self.get_sides()[1]


def get_side3(self):


    return self.get_sides()[2]


def set_sides(self, side1, side2, side3):


    self.set_sides([side1, side2, side3])


class Cube(Fig):


    def __init__(self, side, color):


    super().__init__([side, side, side, side], color)


def get_side(self):


    return self.get_sides()[0]


def set_side(self, side):


    self.set_sides([side, side, side, side])

circle = Circle(5, 'red')
print(circle.get_radius())
circle.set_radius(7)
print(circle.get_radius())

triangle = Triangle(3, 4, 5, 'blue')
print(triangle.get_side1())
print(triangle.get_side2())
print(triangle.get_side3())
triangle.set_sides(6, 7, 8)
print(triangle.get_side1())
print(triangle.get_side2())
print(triangle.get_side3())

cube = Cube(2, 'green')
print(cube.get_side())
cube.set_side(4)
print(cube.get_side())
```
