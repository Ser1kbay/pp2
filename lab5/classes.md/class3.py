class Shape:
    def __init__(a):
        pass

    def area(a):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(int(input()), int(input()))  
print("Area of the rectangle:", rectangle.area())

