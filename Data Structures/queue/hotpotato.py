class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.insert(0, item)
    def dequeue(self):
        return self.queue.pop()
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return self.queue == []

def hotPotato(people, iteration):
    length = len(people)
    q = Queue()

    for x in people:
        q.enqueue(x)

    while(q.size() > 1):
        for i in range(0, iteration):
            item = q.dequeue()
            q.enqueue(item)

        q.dequeue()

    return q.dequeue()

print hotPotato(["Hemang", "Rahul", "Totem", "Hero"], 7)
