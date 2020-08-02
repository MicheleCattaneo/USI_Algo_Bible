'''
Given unlimited supply of coins, find the way to add up to the given number
the coins to make that number.
    Ex: coins ={1,2,3} V=5
    Output: 5 possiblities {1,1,1,1,1} {1,1,1,2}, {1,2,2}, {1,1,3} {2,3}
'''

def makeChangeIter(coins, n):
    # MAKE DP
    DP = []
    for i in range(len(coins)+1):
        col = []
        for j in range(n+1):
            if j==0: # first column is 0, you can always reach 0 with any subsequence of coins
                col.append(1)
            else:
                col.append(0)
        DP.append(col)
    # SOLVE
    for i in range(1, len(DP)):
        for j in range(1, len(DP[0])):
            # if the current coin is bigger than the sum we want, just pick the solution
            # without that coin, meaning a row above
            if coins[i-1] > n:
                DP[i][j] = DP[i-1][j]
            # otherwise we sum the possibilities without taking that coin ( row above )
            # and the possibilities of arriving a the current sub-sum, without that coin ( column j-value of the coin )
            else:
                coinNotPicked = DP[i-1][j]
                coinPicked = DP[i][j-coins[i-1]]
                DP[i][j] = coinNotPicked + coinPicked
    # solution is in the corner
    print(DP[len(coins)][n])


def makeChange(coins, n, acc):
    if n == 0:
        return acc
    if n < 0:
        return None

    for c in coins:
        res = makeChange(coins, n - c, acc+"+"+str(c))

        if res is not None:
            print(res)

    return None



coin1 = [1,3,5,7]
coin2 = [1,2,3]
makeChangeIter(coin2, 5)
makeChangeIter(coin1, 8)

makeChange(coin1, 8, "")
