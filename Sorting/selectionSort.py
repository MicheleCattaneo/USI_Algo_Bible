def selectionSort(A):
    for i in range(len(A) - 1):
        smallest = i
        for j in range(i + 1, len(A)):
            if A[j] < A[smallest]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]
        print(A)
    return A

A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

selectionSort(A)