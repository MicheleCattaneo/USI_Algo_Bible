'''
Given a strign of numbers, it is possible to insert some '+' signs so that
the expression is equal to some number?
'''


global counter

def plusPuzzle(S, target):
    global counter
    counter = 0

    return plusPuzzle_(S, target, {})

def plusPuzzle_(S, target, memo):

    if (S, target) in memo: # if I already computed this problem
        # UNCOMMENT HERE TO SEE HOW MANY TIMES WE ACTUALLY JUST READ A VALUE INSTEAD OF DOING A
        # RECURSIVE CALL:
        #global counter
        #print(counter)
        #counter += 1
        return memo[(S, target)]

    elif int(S) < target: # if target too big
        res = None

    elif int(S) == target: # if exactly the target
        res = S
    else:
        res = None
        for i in range(1, len(S)): # for each possible wy of splitting S in 2 parts
            head = S[:i]
            tail = S[i:]

            headValue = int(head)
            tailSolution = plusPuzzle_(tail, target - headValue, memo)

            if tailSolution is not None:
                res = str(headValue) + '+' + str(tailSolution)
                break

    # put result in memory for future use
    memo[(S, target)] = res
    return res


print(plusPuzzle("213478", 214))
print(plusPuzzle("112233445566778899", 495))
print(plusPuzzle("111222333444555666777888999", 4995))