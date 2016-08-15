
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

n = int(input())
while (n > 0):
    n = n - 1
    x = str(input())
    a, b = x.split(' ')
    aS = Stack()
    bS = Stack()
    for x in a:
        aS.push(int(x))
    for y in b:
        bS.push(int(y))
    string1 = ""
    string2 = ""
    while (aS.isEmpty() == False):
        string1 += str(aS.pop())
    while (bS.isEmpty() == False):
        string2 += str(bS.pop())

    # print("String1" + string1)
    digit1 = int(string1)
    digit2 = int(string2)

    sum = digit1 + digit2

    sS = Stack()
    sumString = str(sum)

    for x in sumString:
        sS.push(int(x))

    result = ""

    length = sS.size()

    while (length > 0):
        length = length - 1
        item = sS.pop()
        if (item != 0):
            sS.push(item)
            break

    while (sS.isEmpty() == False):
        result += str(sS.pop())
    print(result)
