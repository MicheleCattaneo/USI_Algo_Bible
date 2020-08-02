'''
Priority Queue for the class Node =
'''
import math
from GraphTheory.Node import Node


class NodePQ:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return math.floor((i-1) / 2)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def enqueue(self, Node):
        self.heap.append(Node)
        i = self.size
        self.size += 1

        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def find(self, Node):
        id = Node.id
        return self.find_(0, Node)

    def find_(self, root, Node):
        if root >= self.size:
            return -1
        if self.heap[root].id == Node.id:
            return root
        if self.heap[root] < Node:
            left = self.find_(self.left(root), Node)
            if left != -1:
                return left

            right = self.find_(self.right(root), Node)
            if right != -1:
                return right

        return -1

    def decreasePriority(self, Node, value):
        i = self.find(Node)
        if i == -1:
            print("Node not found")
        else:
            currentPrio = self.heap[i].path
            if value > currentPrio:
                print("New value is bigger")
            else:
                self.heap[i].path = value
                while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
                    self.swap(i, self.parent(i))
                    i = self.parent(i)

    def dequeue(self):
        if self.size == 0:
            return None

        head = self.heap[0]
        self.heap[0] = self.heap[self.size -1]
        del self.heap[-1]

        self.size -= 1
        self.minHeapify(0)

        return head

    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l < self.size and self.heap[l] < self.heap[i]:
            smaller = l
        else:
            smaller = i

        if r < self.size and self.heap[r] < self.heap[smaller]:
            smaller = r

        if smaller != i: #if changed
            self.swap(i, smaller)
            self.minHeapify(smaller)

    def printPQ(self):
        for n in self.heap:
            print(n, end=' | ')
        print("")

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def isEmpty(self):
        return self.size == 0

'''
print("yo")
Q = NodePQ()
Q.enqueue(Node(1, 30))
Q.enqueue(Node(2,10))
Q.enqueue(Node(3,5))
Q.printPQ()
Q.decreasePriority(Node(2,10), 2)
Q.printPQ()
Q.dequeue()
Q.printPQ()
Q.dequeue()
Q.printPQ()
'''

