class Node:
    """Create a class for Node type object"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, newNext):
        self.next = newNext


a = Node(3)
b = Node(5)
a.setNext(b)

print(a.data)
print(a.next)
print(a.next.getData())
print(a.getData())
print(a.getNext().getData())

class UnorderedList:
    """ This is an Unordered List Class! """
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None

        while(current != None):
            if(current.getData() == item):
                previous = current.getNext()
                return True
            else:
                previous = current
                current = current.getNext()
        return False

    def search(self, item):
        current = self.head

        while(current != None):
            if(current.getData() == item):
                return True
            else:
                current = current.getNext()
        return False

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head

        while(current != None):
            count = count+1
            current = current.getNext()

        return count

    def append(self, item):
        current = self.head

        while(current != None):
            current = current.getNext()

        current.setData(item)

    def index(self):
        current = self.head
        index = 0

        while(current != None):
            if(current.getData() == item):
                return index
            index += 1
            current = current.getNext()

        return -1

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0

        while(current != None):
            if(count == pos):
                temp = Node(item)
                temp.setNext(current)
                previous.setNext(temp)
                return
            previous = current
            current = current.getNext()
            count += 1

        if(pos > count):
            temp = Node(item)
            previous.setNext(temp)
            return

    def pop(self):
        current = self.head
        previous = None

        while(current.getNext() != None):
            previous = current
            current = current.getNext()

        item = previous.getData()
        previous.setNext(None)

        return item

    def pop(self, pos):
        count = 0
        current = self.head
        previous = None

        while(current != None):
            if(count == pos):
                item  = previous.getData()
                previous.setNext(None)
                return item

            count+=1
            previous = current
            current = current.getNext()
