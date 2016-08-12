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
    def __str__(self):
        stack_str = ""
        for x in self.stack:
            stack_str += x
        return stack_str


list1 = Stack()
list2 = Stack()
def stringToStack(string):
    for x in string:
        list1.push(x)

def makeListTwo(list):
    length = list.size()/2
    while(length > 0):
        list2.push(list1.pop())
        length = length - 1
def compareLists(list1, list2):
    print(list1)
    print(list2)
    return

def doTask():
    stringToStack("abba")
    makeListTwo(list1)
    print(compareLists(list1, list2))

doTask()
