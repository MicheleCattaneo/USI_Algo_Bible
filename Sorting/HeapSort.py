import math
# Heap Sort implementation following the book "Introduction To Algorithms"
# by CLRS ( Third edition )
# implemented by M. Cattaneo


def parent(i):
    return math.floor((i-1) / 2)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest, heap_size)

# The elements in the subarray A[ floor(n/2) + 1 ... n] are all leaves
# Because a tree that is full has as many leaves as nodes remaining
# Therefore the leaves themselves are valid 1-element heaps ( their sub-tree, which is not existing,
# is stays in the heap conditions ). Therefore we need to "heapify" all nodes BOTTOM-UP from
# A[floor(n/2)] to A[0]
def build_max_heap(A):
    i = int((math.floor(len(A)-1)) / 2)
    while i >= 0:
        max_heapify(A, i, len(A))
        i -= 1

# Given an array the make it be a max-heap.
# We know that A[0] will now hold the biggest number in the heap.
# For that reason we swap A[0] with the last element in the array.
# Now the biggest number will be at the end of the array, but the max_heap is not guarantee
# to follow the conditions from position 0. For that reason we decrease the heap size of 1
# ( because we dont consider the last element anymore, it is at its final position) and heapify the
# remaining elements.
def heap_sort(A):
    build_max_heap(A)
    i = len(A)-1
    heap_size = len(A)

    while i >= 1:
        temp = A[0] # the max for this heap-size
        A[0] = A[i]
        A[i] = temp
        heap_size -= 1
        max_heapify(A, 0, heap_size)
        i -= 1



# TESTING
def validate_heap(H):
    i = len(H)-1
    while i > 0:
        if H[parent(i)] < H[i]:
            return False
        i -= 1
    return True

# A Valid max heap ( page 152 of the third edition, Chapter 6, figure 6.1 )
MAX_HEAP = [16,14,10,8,7,9,3,2,4,1]
# A max heap that is not valid in the sub-tree of the node 4 ( index 1 )
# Figure 6.2 (a) of Chapter 6
NOT_HEAP_FROM_INDEX_1 = [16,4,10,14,7,9,3,2,8,1]
assert validate_heap(NOT_HEAP_FROM_INDEX_1) == False
# Heapify the array and check that we obtain the valid max heap
max_heapify(NOT_HEAP_FROM_INDEX_1, 1, len(NOT_HEAP_FROM_INDEX_1))
assert validate_heap(NOT_HEAP_FROM_INDEX_1)
assert MAX_HEAP == NOT_HEAP_FROM_INDEX_1

# Not valid heap ( Figure 6.3 (a) )
TOTALLY_NOT_A_HEAP = [4,1,3,2,16,9,10,14,8,7]
build_max_heap(TOTALLY_NOT_A_HEAP)
assert validate_heap(TOTALLY_NOT_A_HEAP)
# Build a max heap out of that array and check that we obtain the valid max heap
assert MAX_HEAP == TOTALLY_NOT_A_HEAP

A = [1,2,6,9,3,6,4,3,7,6,10]
heap_sort(A)
print(A)

A = [10,9,8,7,6,5,4,3,2,1]
heap_sort(A)
print(A)

