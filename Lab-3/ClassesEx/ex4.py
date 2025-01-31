class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print("x : ", self.x, " y : ", self.y)

    def move(self):
        new_x = int(input("Write new x : "))
        new_y = int(input("Write new y : "))

        self.x = new_x
        self.y = new_y

    def dist(self):
        print("The distance between 2 points is : ", abs(self.x - self.y))

point = Point(4, 9)
point.show()
point.dist()

point.move()

point.show()
point.dist()
