#Program to validate parenthesis
#Using Stack

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def top(self):
        if(self.size()!=0):
            item = self.stack[self.size()-1]
            return item

    def size(self):
        return len(self.stack)


def parenthesisCheck(string):
    """ Function to check parenthesis using Stack class """
    s = Stack()
    length = len(string)

    for x in range(0, length):
        if(string[x] == '('):
            s.push(string[x])
        elif(string[x] == ')' and s.isEmpty() == False):
            s.pop()

    if(s.isEmpty()):
        return True
    else:
        return False

print(parenthesisCheck("(()(()")) #False
print(parenthesisCheck("(())"))   #True
