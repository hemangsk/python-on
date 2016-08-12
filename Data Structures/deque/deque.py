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
