#Program to validate Brackets of all kinds [, {, (
#Using Stack

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if(self.size()!=0):
            return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def top(self):
        return self.stack[self.size()-1]

    def size(self):
        return len(self.stack)

def parenthesisCheck(string):
    s = Stack()
    length = len(string)

    for x in range(0, length):
        item = string[x]
        if item in "{[(":
            s.push(item)
        elif item in "}])" and s.isEmpty() == False:
            popItem = s.pop()
            if (popItem == '(' and item!= ')') or (popItem == '{' and item!='}') or (popItem == '[' and item!=']'):
                return False
        else:
            return False
    if s.isEmpty():
        return True
    else:
        return False

print(parenthesisCheck("{()"))
print(parenthesisCheck("{{([][])}()}"))
print(parenthesisCheck("[{()]"))
