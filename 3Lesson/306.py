class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
n=input()
b = list(map(int,n.split()))
sq = Rectangle(b[0],b[1])
print(sq.area())