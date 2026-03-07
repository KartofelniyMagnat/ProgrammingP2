class Circle:
    def __init__ (self, radius):
        self.radius = radius
    def getRadius(self,radius):
        self.radius = radius
    def area(self,radius):
        print(self.radius*3.12159)
a = Circle()
b=int(input())
a.getRadius(b)
a.area()