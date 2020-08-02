'''
Consider the following maximum-value contiguous subsequence problem: given a
sequence of numbers A = ha1, a2, . . . , ani, find two positions i and j, with 1 ≤ i ≤ j ≤ n, such that
the sum ai + ai+1 + · · · + aj is maximal.
'''

def maxContinuousSubsequence(A):


    i = 1
    maxSequence = [A[0]] # this will be the optimal solution
    maxSum = A[0]
    maxStart = 0

    currSequence = [A[0]] # this is a current solution.
    currentSum = A[0] # it will only change if a single element alone is better than this whole current solution
    currStart = 0 #

    while i < len(A):

        running_sum = currentSum + A[i]

        if running_sum < A[i]: # if the single element is better than the whole current solution, reset everything
            currentSum = A[i]
            currSequence = [A[i]]
            currStart = i

        else: # otherwise we add the element to the current solution, because it might lead to a better solution
            currentSum += A[i]
            currSequence.append(A[i])


        if (currentSum > maxSum): # if the current solution is better than the max solution, update best solution
            maxStart = currStart
            maxSum = currentSum

            maxSequence = copy(currSequence)


        i += 1

    print("Best seq:", maxSequence, "starting at:", maxStart, " adding up to:", maxSum)

def copy(A):
    B = []
    for a in A:
        B.append(a)
    return B

maxContinuousSubsequence([-2, 3, -16, 100, -4, 5])
maxContinuousSubsequence([100, -99, 200, 200, -20, 170])
maxContinuousSubsequence([-2, -17, 100, -80, 90, -200])