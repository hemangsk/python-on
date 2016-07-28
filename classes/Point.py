class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

p = Point()
q = Point()

print(p)
