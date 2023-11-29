class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

def print_area(shape):
    print("Area:", shape.area())

rectangle_instance = Rectangle(11, 10)
circle_instance = Circle(9)

print("Rectangle:")
print_area(rectangle_instance)

print("\nCircle:")
print_area(circle_instance)


