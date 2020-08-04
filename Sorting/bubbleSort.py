def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                print(A)
    return A

A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

bubbleSort(A)