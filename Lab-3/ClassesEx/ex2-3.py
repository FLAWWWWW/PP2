class Shape:
    def area(self):
        print("Area of shape : ", 0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Area of square : ", self.length * self.length)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of rectangle : ", self.length * self.width)

square = Square(3)
square.area()

rectangle = Rectangle(3, 4)
rectangle.area()

shape = Shape()
shape.area()