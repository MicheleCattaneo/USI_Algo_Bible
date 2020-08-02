'''
Consider the subset-sum problem: given a set of numbers A = {a1, a2, . . . , an} and
a number x, output true if there is a subset of numbers in A that add up to x, otherwise output
false. Formally, ∃S ⊆ A such that P
y∈S y = x. Write a dynamic-programming algorithm to solve
the subset-sum problem and informally analyze its complexity.
'''

# Return the String representing the element of the subset that add up to the target
# or None if there exist no solution
def subset(A, target):
    res = subset_(A, target, {})
    if res is None:
        print("No solution for", target)
    else:
        print(res, "=", target)
    return res

def subset_(A, target, memo):
    # if a solution for this sub problem was already computed
    if (str(A), target) in memo:
        return memo[(str(A), target)]

    # first base case
    if len(A) == 0:
        res = None
    # second base case
    elif A[0] == target:
        res = A[0]
    # otherwise we can try to reach the sum by either taking or not taking the first element of A
    else:
        res = None
        head = A[0]
        tail = A[1:]

        # Try if a solution without the head is possible and only after try with the head.
        # This results in having the smallest solution possible.
        # If we want the longest solution possible we can just first compute the one with the head
        # and only if there's not we compute without the head

        pos1 = subset_(tail, target, memo)  # try without taking first element
        if pos1 != None: # if I have a solution without the head
            res = pos1

        else:
            pos2 = subset_(tail, target - head, memo)  # try by taking first element and decreasing target
            if pos2 != None:
                res = str(head) + '+' + str(pos2)

    # Put sub-problem in memory and return it
    memo[(str(A), target)] = res
    return res


# Given a string representing a sum, calculate the value
# ex: "1+-2+3+-1" -> 1
def evaluate(A):
    if A is None:
        return A
    sum = 0
    xs = list(A)
    add = True
    for x in xs:
        if x == '+':
            add = True
        elif x == '-':
            add = False
        elif add:
            sum += int(x)
        else:
            sum -= int(x)

    return sum



def subsetBottomUp(S, target):
    # the arrays of partial sums ( right to left ) of negatives and positives
    pos, neg = partialSums(S)

    return helper_(S, 0, target, pos, neg)

def helper_(S, i, target, pos, neg):
    # if the target is 0, solution is possible
    if target == 0:
        return True
    # if and is reached, no solution is possible
    if i == len(S):
        return False

    if target > pos[i]: # there's no way to add up to target on the right side of S[i]
        return False
    if target < neg[i]: # there's no way go arrive lower on the right side of S[i]
        return False
    # try taking the element ( descrease the target )
    taken = helper_(S, i+1, target - S[i], pos, neg)
    # try not taking the element ( only change index )
    notTaken = helper_(S, i+1, target, pos, neg)

    return taken or notTaken


def partialSums(S):
    '''
    Compute for each position i in the array the sum of positive integers and the sum of negative integers
    that I can still obtain from i+1 to the end of the array
    :param S: the array to check
    :return: the two arrays with the partial sums
    '''
    resPos = [0]*len(S)
    resNeg = [0]*len(S)
    i = len(S)-1
    resPos[i] = S[i] if S[i] > 0 else 0
    resNeg[i] = S[i] if S[i] < 0 else 0
    partialPosSum = resPos[i] # sum of positives so far
    partialNegSum = resNeg[i] # sum of negatives so far
    i -= 1
    while i >= 0:
        curr = S[i]
        if curr > 0: # if curr element is positive, add to positives
            resPos[i] = partialPosSum + curr
            resNeg[i] = partialNegSum
            partialPosSum += curr
        else: # otherwise add to neatives
            resPos[i] = partialPosSum
            resNeg[i] = partialNegSum + curr
            partialNegSum += curr
        i -= 1
    return resPos, resNeg




A1 = [1,3,5,-8,-3,2,2]
#print(partialSums(A1))
print(subsetBottomUp(A1, -6))


#TEST

A1 = [1,3,5,-8,-3,2,2]
assert evaluate(subset(A1, 0)) == 0
assert evaluate(subset(A1, 10)) == 10
assert evaluate(subset(A1, 4)) == 4
assert evaluate(subset(A1, -12)) == None
assert evaluate(subset(A1, -10)) == -10
assert evaluate(subset(A1, -4)) == -4
