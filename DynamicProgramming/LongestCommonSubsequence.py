

def longestCommonSubsequence(S, Q):
    memo = makeMemo(len(S), len(Q))
    return LCS(S, Q, memo)

def LCS(S, Q, memo):

    # If I already have the solution for the length of the current strings
    if memo[len(S)-1][len(Q)-1] is not None:
        return memo[len(S)-1][len(Q)-1]

    # if the length is 0
    if len(S) == 0 or len(Q) == 0:
        res = 0
    else:

        s0 = S[-1] #first char
        s = S[:-1] #rest of the string

        q0 = Q[-1] # first char
        q = Q[:-1] # rest of the string

        # if the last character is the same, the solution is 1 + the solution for the rest of the strings
        if s0 == q0:
            res = 1 + LCS(s, q, memo)
        # otherwise is the best between the solution with S as a whole and rest of Q
        # or the solution with rest of S and Q as a whole
        else:
            pos1 = LCS(s, Q, memo)
            pos2 = LCS(S, q, memo)
            res = max(pos1, pos2)
    memo[len(S)-1][len(Q)-1] = res
    return res

# returns a memo table with the given sizes
def makeMemo(n,m):
    memo = []
    for i in range(n):
        memo.append([None]*m)
    return memo


print(longestCommonSubsequence("BATD", "ABACD"))
print(longestCommonSubsequence("ABCEGHTRS", "CGHRS"))
print(longestCommonSubsequence("123456789", "24680"))