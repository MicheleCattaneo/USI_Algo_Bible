'''
Write an algorithm Sums-One-Two-Three(n) that takes an integer n and, in
time O(n), returns the number of possible ways to write n as a sum of 1, 2, and 3. For
example, Sums-One-Two-Three(4) must return 7 because there are 7 ways to write 4 as a
sum of ones, twos, and threes (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1).
Analyze the complexity of your solution. Hint: use dynamic programming.
'''

def sumOneTwoThree(n):
    return sumOneTwoThree_(n, {})

def sumOneTwoThree_(n, memo):
    if n in memo:
        #print("yo")
        return memo[n]
    else:
        if n <= 0:
            res = 0
        elif n == 1:
            res = 1
        elif n == 2:
            res = 2
        elif n == 3:
            res =4
        else:
            res = sumOneTwoThree_(n-1, memo) + \
                  sumOneTwoThree_(n-2, memo) + \
                  sumOneTwoThree_(n-3, memo)
    memo[n] = res
    return res

def sumOneTwoThreeIterative(n):
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    # iteration
    a = 1 # solution for n-3
    b = 2 # solution for n-2
    c = 4 # solution for n-1
    res = a + b + c # solution for n
    i = 4
    while i < n:
        a = b
        b = c
        c = res
        res = a + b + c
        i += 1

    return res

print(sumOneTwoThree(4))
print(sumOneTwoThree(60))
print(sumOneTwoThree(900))

print("")

print(sumOneTwoThreeIterative(4))
print(sumOneTwoThreeIterative(60))
print(sumOneTwoThreeIterative(900))
# this is not possible with the recursive solution !!
# its a huge number
print(sumOneTwoThreeIterative(6000))