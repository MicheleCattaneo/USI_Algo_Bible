def insertionSort(A):
	i = 1
	while i < len(A):
		k = i
		while k > 0 and A[k] < A[k - 1]:
			A[k], A[k - 1] = A[k - 1], A[k]
			print(A)
			k -= 1
		i += 1
	return A

A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

insertionSort(A)