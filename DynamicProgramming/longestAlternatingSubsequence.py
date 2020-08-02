'''
Return the longest subsequence that is alternating, x < y > z < k .....
Like: 1 < 2 > 0 < 3 > 1 < 5
'''

def longestAlternating(S):
    # either start by going up
    pos1 = longestAlternating_(S, 0, float("-inf"), True)
    # or start by going down
    pos2 = longestAlternating_(S, 0, float("inf"), False)

    # return the longest of the two
    if len(pos1) > len(pos2):
        return pos1
    return pos2

def longestAlternating_(S, i, prev, up):
    #base case
    if i == len(S):
        return ""
    # try not considering the current element
    exclude = longestAlternating_(S, i+1, prev, up)

    include = ""
    # consider this element
    # "up" means "does the sequence need to do up now?"
    if up:
        if S[i] > prev: # curr element needs to be greater, since we want to go up
            include = str(S[i]) +" "+ longestAlternating_(S, i+1, S[i], False)
    else:
        if S[i] < prev:
            include = str(S[i]) +" "+ longestAlternating_(S, i+1, S[i], True)

    if len(exclude) > len(include):
        return exclude
    else:
        return include


S1 = [8,9,6,4,5,7,3,2,4]
print(longestAlternating(S1))