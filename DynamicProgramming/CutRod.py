'''
Given a rod of length n and a table of prices p_1, ..., p_n
determine the maximum revenue r obtainable by cutting up the rod.

'''

def cutRod(prices):
    # returns tuple with best value and length of the cuts
    return cutRod_(prices, len(prices), {})

def cutRod_(prices, length, memo):

    if length in memo: # if in memo

        return memo[length]

    if length == 0: # if length == 0, no value
        res = (0, "")
    elif length == 1: # if lengh == 1, only 1 possible solution
        res = (prices[0], "1")

    # otherwise try all possible ways to cut the current rod into sub-rods:
    # meaning: keep a piece of length i and search solution for ( length - i )
    else:
        res = (float("-inf"), "")
        for i in range(1, length + 1):

            currentPiece = prices[i-1]
            subProblem = cutRod_(prices, length - i, memo)

            pos = currentPiece + subProblem[0]

            if pos > res[0]:
                # if got a new best solution, create tuple with tha best solution and
                # add the length of the piece take to the solution of the subproblem
                res = (pos, str(i) + " " + subProblem[1])

    memo[length] = res
    return res


p1 = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
p2 = [1, 5, 8, 9, 10] 

print(cutRod(p1))
print(cutRod(p2))
