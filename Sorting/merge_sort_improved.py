import sys
import math
import random
import time
#improved version of a merge sort, using insertion sort for subarrays of length <= 5

#Execute insertion sort only on the given subarray indices
#
def insertion_sort(A, l, r):
    for i in range(l, r+1):
        j=i-1
        curr = A[i]
        while j >= 0 and A[j] > curr:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = curr

def merge(A, l, m, r):

    left_length = m - l + 1
    right_length = r - m
    L = [0]*(left_length+1)
    R = [0]*(right_length+1)

    for i in range(left_length):
        L[i] = A[l + i]
    for i in range(right_length):
        R[i] = A[m + i + 1]

    L[left_length] = R[right_length] = sys.maxsize #INF.

    j = i = 0
    for k in range(l, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort_helper(A, l, r, k):
    if (r - l) <= k:
        m = math.floor((l+r)/2)
        merge_sort_helper(A, l, m, k)
        merge_sort_helper(A, m+1, r, k)
        merge(A, l, m, r)
    else:
        insertion_sort(A, l, r)
    return A

def merge_sort(A, k):
    return merge_sort_helper(A, 0, len(A)-1, k)


# k must be smaller that le array length divided by 2!
#k = int(sys.stdin.readline())
test_array = [random.randint(-99, 99) for iter in range(10000)]
t0 = time.time()
merge_sort(test_array, 10)
t1 = time.time()
print(t1-t0)
#print(test_array)
# TESTING
"""

def control(A):
    A.sort()
    return A

START = -99
STOP = 99
LIMIT = 1000

RANDOM1 = [random.randint(START, STOP) for iter in range(LIMIT)]
#print(RANDOM1)
RANDOM2 = [random.randint(START, STOP) for iter in range(LIMIT)]
#print(RANDOM2)
RANDOM3 = [random.randint(START, STOP) for iter in range(LIMIT)]
#print(RANDOM3)
A1 = [3,2,1,4,5,0,8,7]
A2 = [10,9,8,7,6,5,4,3,2,1]
A3 = [10,0,9,2,8,3,7,4,6,5]

assert merge_sort(A1) == control(A1)
print(A1)
assert merge_sort(A2) == control(A2)
print(A2)
assert merge_sort(A3) == control(A3)
print(A3)
assert merge_sort(RANDOM1) == control(RANDOM1)
assert merge_sort(RANDOM2) == control(RANDOM2)
assert merge_sort(RANDOM3) == control(RANDOM3)

"""
