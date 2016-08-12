class Deque:
    def __init__(self):
        self.deque = []
    def addFront(self, item):
        self.deque.insert(0, item)
    def addRear(self, item):
        self.deque.append(item)
    def removeFront(self):
        return self.deque.pop(0)
    def removeRear(self):
        return self.deque.pop()
    def isEmpty(self):
        return self.deque == []
    def size(self):
        return len(self.deque)
    def __str__(self):
        string = ""
        for x in self.deque:
            string +=x
        return string
    def __eq__(self, other):
        return self.deque == other.deque

def checkPalindrome(string):
    d = Deque()
    e = Deque()
    for x in string:
        d.addRear(x)

    for y in string:
        e.addFront(y)

    print(d==e)

checkPalindrome("abbacd")
