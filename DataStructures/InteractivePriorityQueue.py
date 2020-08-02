import sys
import math

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.heap_size = 0
    #return index of the parent of a node in the heap
    def parent(self, i):
        return math.floor(i / 2)
    #return the index of the left child of a node
    def left(self, i):
        return 2 * i + 1
    #return the index of the right child of a node
    def right(self, i):
        return 2 * i + 2

    # Add new entry at the end of the heap and check the heap condition of the new
    # entry ( bottom to top of the tree )
    # overkill in variable use, but it makes it clearer when reading the code
    def enqueue(self, e, p):
        print("you enqueued", e," with priority ",p)
        elem = (e,p)
        if self.heap_size == len(self.heap):
            self.heap.append(elem)
        else:
            self.heap[self.heap_size] = elem
        i = self.heap_size
        parent_index = self.parent(i)
        parent_value = self.heap[parent_index]
        child_index = i
        child_value = self.heap[child_index]
        while child_index > 0 and parent_value[1] < child_value[1]:
            #swap parent and child if they dont follow the heap condition
            self.heap[parent_index] = child_value
            self.heap[child_index] = parent_value
            child_index = parent_index
            child_value = self.heap[child_index]
            parent_index = self.parent(child_index)
            parent_value = self.heap[parent_index]

        self.heap_size += 1


    #returns the maximum value in the queue
    def max(self):
        return self.heap[0]
    #returns and remove the maximum value in the queue
    def dequeue(self):
        max = self.max()
        print("dequeued", max)
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap_size -= 1
        self.max_heapify(0)

        return max
    # restores the heap condition from a given index i where we know
    # that is has been violated
    def max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)

        if l < self.heap_size and self.heap[l][1] > self.heap[i][1]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.heap[r][1] > self.heap[largest][1]:
            largest = r

        if largest != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp
            self.max_heapify(largest)

    # prints the heap from 0 to heap_size
    def print(self):
        for i in range(self.heap_size):
            print(self.heap[i]," ", end='')
        print("")

    #main function: read input and execute commands on the queue
    def main(self):
        for l in sys.stdin:
            l = l.split()
            if len(l) == 0:
                continue
            if l[0] == '+':
                self.enqueue( l[1], int(l[2]))
            elif l[0] == '-':
                self.dequeue()
            elif l[0] == 'print':
                self.print()
            elif l[0] == 'max':
                print(self.max())
            elif l[0] == 'help':
                print("enqueue: + 'item' 'priority' ")
                print("dequeue: -")
                print("print queue: print")
                print("show maximum priority item: max")
                print("quit program: exit")
            elif l[0] == 'exit':
                break
            else:
                print("Unknown command", l[0])
            print("---------------")

queue = PriorityQueue()
queue.main()

