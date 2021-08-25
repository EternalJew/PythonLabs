import math
print("task 2")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getXY(self):
        return [ self.x, self.y ]
    
    def __add__(self, point):
        self.x = self.x - point.x
        self.y = self.y - point.y
        return self

    def Show(self, text):
        print(text, " = (", self.x, "; ", self.y, ")")

pt1 = Point(5, 6)
pt1.Show("pt1")

pt2 = Point(7, 11)
pt2.Show("pt2")

pt3 = pt1 + pt2
pt3.Show("pt3 = pt1 + pt2")
    