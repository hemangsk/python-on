#Base Conversion Using Stack

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
        return self.stack[self.size()-1]
    def size(self):
        return len(self.stack)


digits = "0123456789ABCDEF";

def baseConvert(num, base):
    s = Stack();
    while(num!=0):
        s.push(num%base)
        num = num/base

    result = ""
    while(s.isEmpty() == False):
        result = result + digits[s.pop()]

    return result

print(baseConvert(25,2))
