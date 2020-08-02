'''
    This kind of (doubly) linked list has a speacial Node ( Link ) at the beginning called sentinel
    sentinel.next is the first element of the list ( itself if empty )
    sentinel.prev is the last element of the list ( itself if empty )
    the last element will have the sentinel as next element
'''

class Link:
    def __init__(self):
        self.prev = None
        self.value = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.sentinel = Link()
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
        self.size = 0

    # Insert a value after the given Link
    def insertAfter(self, l, value):
        new = Link()
        new.value = value
        right_pointer = l.next

        l.next = new
        new.next = right_pointer
        right_pointer.prev = new
        new.prev = l

        self.size += 1

    # Delete the Link that comes after the given one
    def deleteAfter(self,l):
        to_delete = l.next #rip
        new_pointer = to_delete.next
        l.next = new_pointer
        new_pointer.prev = l
        if self.size != 0:
            self.size -= 1

    def append(self, value):
        self.insertAfter(self.sentinel.prev, value)

    def prepend(self,value):
        self.insertAfter(self.sentinel)

    # Inserts at index i, later indices gets shifted by one, it doesnt substitute (increases size)
    def insert(self, v, i):
        if i >= self.size:
            print("index to large")
            return
        index = 0
        curr = self.sentinel
        while index < i:
            curr = curr.next
            index += 1
        self.insertAfter(curr,v)

    # Replace the entry ad the given index with the given value (doesn't increase size)
    def replace(self, v, i):
        if i >= self.size:
            print("index to large")
            return
        index = 0
        curr = self.sentinel
        while index < i:
            curr = curr.next
            index += 1
        self.deleteAfter(curr)
        self.insertAfter(curr, v)

    def deleteLast(self):
        self.deleteAfter(self.sentinel.prev.prev)

    def deleteFirst(self):
        self.deleteAfter(self.sentinel)

    def isEmpty(self):
        return self.sentinel.next == self.sentinel

    def toString(self):
        res = "[" #empty list
        curr = self.sentinel.next
        while curr != self.sentinel:
            res += str(curr.value)+" "
            curr = curr.next
        return res+"]"

    def print(self):
        print(self.toString())


# Trying here


ll = LinkedList()
ll.deleteFirst()
ll.print()
#print(ll.size)
ll.deleteFirst()
ll.print()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print()
#print(ll.size)
ll.deleteLast()
ll.print()
ll.deleteFirst()
ll.print()
ll.insert(99,1)
ll.print()
ll.replace(88, 2)
ll.print()
ll.deleteLast()
ll.deleteLast()
print(ll.isEmpty())
ll.deleteLast()
ll.deleteLast()
print(ll.isEmpty())

#print(ll.size)

