'''
Write an algorithm Maximal-Non-Adjacent-Sequence-Weight(A) that, given a
sequence of numbers A = ha1, a2, ..., ani, computes, with worst-case complexity O(n), the maximal weight of any sub-sequence of non-adjacent elements in A. A sub-sequence of non-adjacent
elements may include ai or ai+1 but not both, for all i. For example, with A = [2, 9, 6, 2, 6, 8, 5],
Maximal-Non-Adjacent-Sequence-Weight(A) should return 20. (Hint: use a dynamic programming algorithm that scans the input sequence once.)
'''

def maxNonAdjecentSequence(A):
    return maxNonAdjecentSequence_(A, {})

def maxNonAdjecentSequence_(A, memo):
    # if I already computed that sum for the sub-problem 'A'
    # Note that a list is not hashable, so we turn it into a string
    if str(A) in memo:
        res = memo[str(A)]
    else:
        # base case: empty list, we have nothing
        if len(A) == 0:
            res = 0
        # base case 2: one element,
        # we can either pick it if it's greater than 0 or dont pick it and end up with a sum of 0
        elif len(A) == 1:
            res = max(0, A[0])
        else:
            # remove 2 elements, because we pick the first, we can not pick the second.
            # at next call we can either pick the 3rd element or not
            pos1 = maxNonAdjecentSequence_(A[2:], memo)
            # remove only one element, hence the one that we do not pick
            # at next call we can either pick the 2nd element or not
            pos2 = maxNonAdjecentSequence_(A[1:], memo)

            res = max(pos2, pos1 + A[0])

    memo[str(A)] = res
    return res

def maxNonAdjBottomUp(S):
    memo = [0]*len(S)
    if len(S) == 0: # base cases
        return None
    if len(S) == 1: # base cases
        return S[0]

    memo[0] = S[0] # easy case
    memo[1] = max(S[0], S[1]) #easy case
    i = 2
    while i < len(S):
        takeIt = memo[i-2] + S[i] # if you take that element, you need to take solution of 2 steps before
        dontTakeIt = memo[i-1] # just take previous solution if you dont take it

        memo[i] = max(S[i], takeIt, dontTakeIt) #S[i] alone could still have a better solution

        i+=1
    return memo[len(S)-1]


print(maxNonAdjecentSequence([2, 9, 6, 2, 6, 8, 5]))
print(maxNonAdjBottomUp([2, 9, 6, 2, 6, 8, 5]))
print(maxNonAdjecentSequence([10,-2,-2,18,-2]))
print(maxNonAdjBottomUp([10,-2,-2,18,-2]))
print(maxNonAdjecentSequence([1,-1,1,-1,1]))
