import random
'''
Given a list of items with an associated weight W[i] and value V[i]
and a capacity C of the sack, return the maximal value possible that
you can put in the sack of that capacity
Author: Michele Cattaneo
'''

def recursiveKnapsack(values, weights, C):
    memo = makeMemo(len(values), C)
    return recursiveKnapsack_(values, weights, C, len(values), memo)

def recursiveKnapsack_(values, weights, C, itemsLeft, memo):

    if memo[itemsLeft-1][C-1] is not None:

        return memo[itemsLeft-1][C-1]

    # since it's a 0 based array
    itemIndex = itemsLeft -1

    # if capacity is 0 or the items left is 0, we dont have any value to return
    if itemsLeft == 0 or C == 0:
        result = 0
    # if the weight of the current item is bigger than the capacity left
    # dont pick that item, so capacity doesnt change
    elif weights[itemIndex] > C:
        result = recursiveKnapsack_(values, weights, C, itemsLeft-1, memo)
    # Pick best solution if choosing to pick that item, or not picking it
    else:
        # if you dont pick that item, simply return solution with 1 item less
        possibility1 = recursiveKnapsack_(values, weights, C, itemsLeft-1, memo)
        # if you pick the item, you have the value of that item + the value of the best solution with 1 item less and the capacity
        # that becomes smaller of the weight of the item picked
        possibility2 = values[itemIndex] + recursiveKnapsack_(values, weights, C - weights[itemIndex], itemsLeft-1, memo)
        # return best of the two
        result = max(possibility1, possibility2)
    memo[itemsLeft-1][C-1] = result
    return result

def makeMemo(n,c):
    memo = []
    for i in range(n):
        memo.append([None]*c)
    return memo

w1 = [1,2,4,2,5]
v1 = [5,3,5,3,2]
print(recursiveKnapsack(v1, w1, 10))
print(recursiveKnapsack(v1, w1, 5))

w2 = [random.randint(0, 100) for iter in range(500)]
v2 = [random.randint(0, 100) for iter in range(500)]
print(recursiveKnapsack(v2, w2, 40))