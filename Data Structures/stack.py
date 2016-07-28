#Oh! You're here? I was searching for you on Jupiter.

#Welcome to DS1O1 - Stack Abstract Data Type

class Stack:

    def __init__(self):
        """ Yeah That Fancy Constructor which creates a new List/Stack everytime """

        self.stack = []

    def push(self, item):
        """ Push item onto stack """
        self.stack.append(item)

    def pop(self):
        """ Pop item from stack """
        item = self.stack.pop()
        return item

    def isEmpty(self):
        """ Check if stack is empty """
        return self.stack == []

    def size(self):
        """ Return the size of stack """
        return len(self.stack)

    def top(self):
        """ Return the topmost element of the stack """
        if(self.size()!=0):
            return self.stack[self.size() - 1]


#Perform some operations

s = Stack()
s.push(8)
s.push(10)
s.push(9)
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())
