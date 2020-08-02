'''

Longest Palindromic Subsequence ( can be not consecutive )

ABBDCACB -> BCACB
'''

def longestPalinSequence(S):
    if len(S) <= 1:
        return S
    else:
        first = S[0] #first char
        last = S[-1] #last char
        body = S[1:-1] # in between

        # if first and last char are the same, include
        # them in the solution and find solution for the middle part
        if first == last:
            return first + longestPalinSequence(body) + last
        else:
            #otherwise find solution including only the first, or only the last
            pos1 = longestPalinSequence(body+last)
            pos2 = longestPalinSequence(first+body)
            res = pos1 if len(pos1) > len(pos2) else pos2

            return res


print(longestPalinSequence("ABBDCACB"))
print(longestPalinSequence("AXBYCSDREPFWFQETDICKBLA"))