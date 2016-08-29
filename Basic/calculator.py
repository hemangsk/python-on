class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def __str__(self):
        return "Values in calc = " + str(self.a) + " and " + str(self.b)


c = Calculator(4,5)
# print c.add()
# print c.sub()
# print c.mult()
print c
