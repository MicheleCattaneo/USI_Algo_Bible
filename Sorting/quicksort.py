import random
#Implementation of a quicksort

# pick a random pivot ( this case last element )
# partition the array in less/equal than pivot and bigger than pivot
def partition(A, begin, end):
    #print("begin", begin, "end", end)

    q = begin
    pivot = A[end]
    print("pivot", pivot)
    for i in range(begin, end+1):
        if A[i] <= pivot:
            temp = A[q]
            A[q] = A[i]
            A[i] = temp
            q += 1
    return q-1

def quicksort_h(A, begin, end):
    # Q is the position of the pivot from the partition
    # therefore its left is less/equal than pivot, its right is greater than pivot
    if begin < end:
        q = partition(A, begin, end)
        print(A)
        quicksort_h(A, begin, q-1)
        quicksort_h(A, q+1, end)

def quicksort(A):
    quicksort_h(A, 0, len(A)-1)
    print("")
    return A

# Testing
def control(A):
    A.sort()
    return A



START = 0
STOP = 99
LIMIT = 10

RANDOM1 = [random.randint(START, STOP) for iter in range(LIMIT)]
#print(RANDOM1)
RANDOM2 = [random.randint(START, STOP) for iter in range(LIMIT)]
#print(RANDOM2)
RANDOM3 = [random.randint(START, STOP) for iter in range(LIMIT)]
#print(RANDOM3)
A1 = [3,2,1,4,5,0,8,7]
A2 = [10,9,8,7,6,5,4,3,2,1]
A3 = [10,0,9,2,8,3,3,7,3,4,6,5]

#print(quicksort(A1))
assert quicksort(A1) == control(A1)
assert quicksort(A2) == control(A2)
assert quicksort(A3) == control(A3)
assert quicksort(RANDOM1) == control(RANDOM1)
assert quicksort(RANDOM2) == control(RANDOM2)
assert quicksort(RANDOM3) == control(RANDOM3)


P1 = [10,0,9,2,8,3,3,7,3,4,6,5]
assert partition(P1,0, len(P1)-1) == 6
assert P1 == [0, 2, 3, 3, 3, 4, 5, 7, 8, 9, 6, 10]

