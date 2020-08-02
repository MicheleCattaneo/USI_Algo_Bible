'''
Given a sequence of numbers A = ha1, a2, . . . , ani, an increasing subsequence is a
sequence ai1
, ai2
, . . . , aik of elements of A such that 1 ≤ i1 < i2 < . . . < ik ≤ n, and such that
ai1 < ai2 < . . . < aik
. You must find the longest increasing subsequence. Solve the problem using
dynamic programming
'''


def incSub(A):
    # initial table full of 1, each subsequence of length 1 is an increasing subsequence
    table = [1]*len(A)

    # keep a pointer i from i to len(A) -1
    # keep a pointer j that for each i, goes from 0 to i-1
    i = 1
    while i < len(A):
        j = 0
        # reset the pointers if they reached each other
        # i goes to the next place and j goes back to 0
        if j == i:
            j = 0
            i += 1
        # otherwise for each j, if A[j] < A[i] it means that we COULD improve the
        # subsequence length.
        # if the solution A[j] + 1 is better than the current solution for A[i] we pick that one.
        else:
            while j < i:

                if A[j] < A[i]:
                    table[i] = max(table[i], table[j]+1)

                j += 1

        i += 1

    return max(table)



def longestIncSubRecursive(S, i, prev):
    end = len(S)
    if i == end:
        return ""
    else:
        # try by not considering the element at i
        exclude = longestIncSubRecursive(S, i+1, prev)
        include = ""
        # if the element at i is grater than the last element considered ( prev ),
        # add it to the possible solution of the rest of the string
        if S[i] > prev:
            include = str(S[i]) + " " + longestIncSubRecursive(S, i+1, S[i])

        #pick longest of the two
        if len(exclude) > len(include):
            return exclude
        else:
            return include





A = [3,4,-1,0,6,2,3]
print(incSub(A)) #only prints length
print(longestIncSubRecursive(A,0, float("-inf"))) #actually prints the sequence

B = [1,-5,2,-3,3,-7,4,5,6]
print(incSub(B))
print(longestIncSubRecursive(B,0, float("-inf")))

C = [1,2,3,4,5,-7,-6,6,7,8,9]
print(incSub(C))
print(longestIncSubRecursive(C,0, float("-inf")))