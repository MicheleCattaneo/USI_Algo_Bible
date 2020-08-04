def mergeSort(A):
    if len(A) > 1:
        print(A)
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i += 1
            else:
                A[k]=righthalf[j]
                j += 1
            k += 1
            print(A)

        while i < len(lefthalf):
            A[k]=lefthalf[i]
            i += 1
            k += 1
            print(A)

        while j < len(righthalf):
            A[k]=righthalf[j]
            j += 1
            k += 1
            print(A)
    return A

A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

mergeSort(A)