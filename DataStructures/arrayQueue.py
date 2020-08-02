class arrayQueue:

    def __init__(self, size):
        self.array = [0]*size
        self.size = size
        self.head = 0
        self.tail = 0

    # if you are at the end of the array, next is the beginning of the array
    def next(self, i):
        if i == self.size - 1:
            return 0
        return i+1

    # if the next position from tail would be the same as head, queue is full
    def isFull(self):
        return self.next(self.tail) == self.head

    def isEmpty(self):
        return self.tail == self.head

    def enqueue(self, v):
        if self.isFull():
            print("overflow")
            return

        # put v in pos of tail
        self.array[self.tail] = v
        # increase tail
        self.tail = self.next(self.tail)

    def dequeue(self):
        if self.isEmpty():
            print("underflow")
            return

        v = self.array[self.head]
        self.head = self.next(self.head)
        return v

    def toString(self):
        res = "head -> "
        i = self.head
        while i != self.tail:
            res += str(self.array[i])+" "
            i = self.next(i)
        res += "<- tail"
        return res

    def print(self):
        print(self.toString())


# "Testing" ( more like trying in a rush )

queue = arrayQueue(10)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print()
queue.dequeue()
queue.print()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.print()
queue.enqueue(9)
queue.enqueue(10)
queue.print()
queue.enqueue(11)
queue.dequeue()
queue.print()
queue.enqueue(11)
queue.print()