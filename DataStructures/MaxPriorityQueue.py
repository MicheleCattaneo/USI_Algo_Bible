import math

class maxPriorityQueue:

    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def __init__(self, numbers):
        self.heap_size = len(numbers)
        self.heap = numbers
        self.build_max_heap()

    def parent(self, i):
        return math.floor((i-1) / 2)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.heap[l] > self.heap[i]:# always check if the index is actually in the bound
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp
            self.max_heapify(largest)

    def build_max_heap(self):
        i = int((math.floor(len(self.heap)-1)) / 2) # -1 or not??
        while i >= 0:
            self.max_heapify(i)
            i -= 1

    def maximum(self):
        if self.heap_size > 0:
            return self.heap[0]
        else:
            raise Exception("heap underflow")

    def pop(self):
        if self.heap_size < 1:
            raise Exception("heap underflow")
        max = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max

    def increaseKey(self, i, key):
        if key < self.heap[i]:
            raise Exception("new key is smaller than current one")
        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            parent = self.parent(i)
            temp = self.heap[parent]
            self.heap[parent] = self.heap[i]
            self.heap[i] = temp
            i = parent

    def insert(self, key):
        self.heap.append(float("-inf"))
        self.heap_size += 1
        self.increaseKey(self.heap_size - 1, key)

#Testing
def isValid(A):
    i = len(A)-1
    while i > 0:
        if A[math.floor((i-1) / 2)] < A[i]:
            return False
        i -= 1
    return True

queue = maxPriorityQueue([4,1,3,2,16,9,10,14,8,7])
assert isValid(queue.heap)
#print(queue.heap)
#print(queue.heap_size)
#queue.pop()
#print(queue.heap)
#print(queue.heap_size)

#already a valid heap
queue2 = maxPriorityQueue([16,14,10,8,7,9,3,2,4,1])
assert isValid(queue2.heap)
#increase the value 4 to be 15
queue2.increaseKey(8, 15)
assert isValid(queue2.heap)
print(queue2.heap)
queue2.insert(200)
assert isValid(queue2.heap)
print(queue2.heap)

i = queue2.heap_size - 1
while i >= 0:
    print(queue2.pop())
    i -= 1