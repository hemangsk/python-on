class Queue:

    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.insert(0,item)

    def dequeue(self):
        return self.q.pop()

    def size(self):
        return len(self.q)

    def isEmpty(self):
        return self.q == []

    def __str__(self):
        res = ""
        length = self.size()
        i = 0
        while(i<length):

            res += str(self.q[i]) + "\n"     # a = int("3")
            i+=1

        return res


myQ = Queue()
myQ.enqueue(9)
myQ.enqueue(10)
print myQ
