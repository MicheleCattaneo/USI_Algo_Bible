'''
Find the longest subsequence that is first increasing and then decreasing ( bi-tonic )

'''

def bitonicSubsequence(S):
    # start from 0, with -inf as prev and going up ( up = True )
    # flag is True only if we already went down, meaning that we can not go up again
    return bitonic(S, 0, float("-inf"), True, False)

def bitonic(S, i, prev, up, flag):
    end = len(S)
    if i == end:
        return ""

    else:
        excludeUp = ""
        # only if we still have not gone down, we can go up, otherwise
        # the sequence resulting could be going up and down multiple times
        if not flag:
            # solution excluding the current char and going up
            excludeUp = bitonic(S, i+1, prev, True, False)
        # solution excluding the current char and going down
        excludeDown = bitonic(S, i+1, prev, False, True)

        includeUp = ""
        includeDown = ""

        # again to check for a solution going up, we need to be sure we still have not gone down,
        # otherwise the sequence could go up and down multiple times, like:  1 2 3 2 1 2 3 2 1
        if S[i] > prev and up == True and not flag:
            # solution including the current char,  going up
            includeUp = str(S[i]) + " " + bitonic(S, i+1, S[i], True, False)

        if S[i] < prev and up == False:
            # solution including the current char, going down and making sure that flag is True
            # flag True = we already went down, cant go up anymore
            includeDown = str(S[i]) + " " + bitonic(S, i+1, S[i], False, True)

        # return the max among the solutions
        return max([excludeUp, excludeDown, includeUp, includeDown], key=len)

S1 = [1,6,2,3,5,4,3,2,1]
print(bitonicSubsequence(S1))

S2 = [5,4,3,2,3,8,10,9,3,2,1]
print(bitonicSubsequence(S2))

