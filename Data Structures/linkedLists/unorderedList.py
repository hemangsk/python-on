class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def setData(self, data):
        self.data = data
    def setNext(self, nextItem):
        self.next = nextItem
    def getData(self):
        return self.data
    def getNext(self):
        return self.next

class UnorderedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        current = self.head
        string = ""
        while(current != None):
            string +=str(current.getData()) +", "
            current = current.getNext()

        string = string[:-2]
        return string
    def isEmpty(self):
        return self.head == None
    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        count = 0
        current = head
        while (current != None):
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        current = head
        found = False
        while(current != None and found != True):
            if(item == current.getData()):
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        found = False
        previous = None
        while(current != None and not found):
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
        if previous == None and found == True:
            self.head = None
        elif previous !=None and found == True:
            previous.setNext(current.getNext())

newList = UnorderedList()
newList.add(3)
newList.add(5)
newList.add(8)
newList.remove(3)
print(newList)
