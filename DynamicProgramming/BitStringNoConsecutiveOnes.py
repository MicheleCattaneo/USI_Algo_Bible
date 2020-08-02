'''
Given a number n find the number of binary strings of length n
without any consecutive 1
'''


def NumberOfBinaryStringNoConsecutiveOne(n):

    memoFinishWith0 = [0]*(n+1)
    memoFinishWIth1 = [0]*(n+1)

    memoFinishWith0[1] = 2 # bit string of length 1 preceeded by a 0 are 2; 1 and 0
    memoFinishWIth1[1] = 1 # bit string of length 1 preceeded by a 1 are 1: 0 ( otherwise there would be a consecutive 1 )

    for i in range(2, n+1):
        j = i-1
        prevWith0 = memoFinishWith0[j] # bitstring smaller by 1 that ends in 0
        prevWith1 = memoFinishWIth1[j] # bitstring smaller by 1 that ends in 1
        memoFinishWith0[i] = prevWith0 + prevWith1 # the current string ends in 0, so we can add both possibilities
        memoFinishWIth1[i] = prevWith0 # can only add the possibility that ends in 0

    return memoFinishWith0[n]


assert NumberOfBinaryStringNoConsecutiveOne(5) == 13
assert NumberOfBinaryStringNoConsecutiveOne(4) == 8