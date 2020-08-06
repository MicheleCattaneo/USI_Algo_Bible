def binarySearch(A, x):
    # Assume A is sorted
    if len(A) == 0:
        return False
    m = len(A) // 2
    if x > A[m]:
        return binarySearch(A[m+1:len(A)], x)
    elif x < A[m]:
        return binarySearch(A[0:m], x)
    else:
        return True

A = [1, 3, 4, 5, 6, 8, 10, 11, 12, 12]

print(binarySearch(A, 88))
print(binarySearch(A, 8))