import sys
import math
import random

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

def merge_sort_helper(A, l, r):
    if l < r:
        m = math.floor((l+r)/2)
        merge_sort_helper(A, l, m)
        merge_sort_helper(A, m+1, r)
        merge(A, l, m, r)
    return A

def merge_sort(A):
    return merge_sort_helper(A, 0, len(A)-1)

A = [7,6,5,4,3,2,1]
merge_sort(A)
print(A)
# TESTING

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
assert merge_sort(A2) == control(A2)
assert merge_sort(A3) == control(A3)
assert merge_sort(RANDOM1) == control(RANDOM1)
assert merge_sort(RANDOM2) == control(RANDOM2)
assert merge_sort(RANDOM3) == control(RANDOM3)
