'''
    Given a list of coins, find the minimum number of coins to get to a certain value
    For Example: coins={1,2,3} V=5
    Output: 2 (3+2=5)
    Note: the list must always contain a coin of value 1, so in the worst case the output will be V*'coin 1'
'''
def minCoin(coins, amount):
    return minCoin_(coins, amount, {})

def minCoin_(coins, amount, memo):

    if amount in memo:

        return memo[amount]

    if amount <= 0:
        res = 0
    else:
        res = float("inf")

        for c in coins: # try taking each coin
            pos = 1 + minCoin_(coins, amount - c, memo) #take the coin and look for solution with that value less
            if pos < res: # if it's a better solution
                res = pos
    memo[amount] = res
    return res

def minCoinIter(coins, amount):

    memo = [float("inf")]*(amount+1)
    memo[0] = 0 # 0 coins needed to read 0

    for amt in range(1, amount+1): # for each sub-amount
        # amt is the current amount

        for c in coins: # for each coin c
            if c <= amt:
                # we can take that coin by looking at the solution with the amount
                # being lowered by c, and adding 1 because we take that coin
                takeThatCoin = memo[amt - c] + 1
                # is it a better solution?
                memo[amt] = min(memo[amt], takeThatCoin)

    # last position of memo contain the solution for amt = amount
    return memo[amount-1]




c1 = [1,2,3]
print(minCoin(c1, 3))
print(minCoin(c1, 5))
print(minCoin(c1, 20))

print(minCoinIter(c1, 20))
# only possible with an iterative approach!
# resursion depth limit would be reached using the resursive solution
print(minCoinIter(c1, 1000))