class Stack:
    """docstring for stack."""
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[self.size()-1]
    def isEmpty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)

def infix2postFix(string):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 3
    prec["-"] = 3
    prec["("] = 1

    s = Stack()
    expression = string.split(' ')
    result = ""

    for x in expression:
        if x == "(":
            s.push(x)

        elif x == ")":
            item = s.pop()
            while(item != "("):
                result += item
                item = s.pop()

        elif x in "1234567890" or x in "abcdefghijklmnopqrstuvwxyz":
            result +=x

        elif x in "*/-+" and s.size() != 0:
            if s.peek() in "*/+-":
                while(prec[s.peek()] >= prec[x] ):
                    result+=s.pop()
                s.push(x)
            s.push(x)

        elif x in "*/-+":
            s.push(x)

    leftStack = s.size()

    while(leftStack > 0):
        result+=s.pop()
        leftStack -= 1
    return result

print(infix2postFix("9 + 3"))
