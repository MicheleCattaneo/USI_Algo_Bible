'''
    Find the subsequence which has the biggest sum:
    S is the sequence
    i current index
    prev previous element picked
    sum the current sum
    seq the sequence that adds up to that sum
'''

def maxIncSub(S):
    return maxIncSub_(S, 0, float("-inf"), 0, "")

def maxIncSub_(S, i, prev, sum, seq):
    end = len(S)
    if i == end:
        return seq, sum

    else:
        exclude = maxIncSub_(S, i+1, prev, sum, seq)

        include = "", 0
        if S[i] > prev:
            include = maxIncSub_(S, i+1, S[i], sum+S[i], seq +" "+ str(S[i]))

        if exclude[1] > include[1]:
            return exclude
        else:
            return include

S1 = [1,2,3,4,2,1,14,15,1,2,6,3,2,16,17]
S2 = [1,2,2,-1,3,4,7,5,6,10]

print(maxIncSub(S1))
print(maxIncSub(S2))
