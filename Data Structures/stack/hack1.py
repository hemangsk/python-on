# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
"""
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

"""

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)
    def top(self):
        return self.stack[self.size() - 1]
    def getMax(self):
        return max(self.stack)

n = int(sys.stdin.readline())
s= Stack()
while(n>0):
    n-=1
    option = sys.stdin.readline()
    input_list = option.split()
    if(len(input_list) == 2 and int(input_list[0]) == 1):
        item = int(input_list[1])
        s.push(item)
    elif(int(option) == 2):
        if s.isEmpty() == False:
            s.pop()
    elif(int(option) == 3):
        print (s.getMax())
