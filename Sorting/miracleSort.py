def miracleSort(A):
    sorted = True

    for i in range(len(A) - 1):
        if (A[i] < A[i + 1]):
            sorted = False

    if (sorted):
        return A
    else:
        miracleSort(A)

A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

miracleSort(A)