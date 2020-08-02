'''
Consider the following game: you are given a set of n valuable objects placed on a
2D plane with non-negative x, y coordinates. In practice, you are given three arrays X, Y, V, such
that X[i], Y [i], and V [i] are the x and y coordinates and the value of object i, respectively. You
start from position 0, 0, and can only move horizontally to the right (increasing your x coordinate)
or vertically upward (increasing your y coordinate). Your goal is to reach and collect valuable
objects. Write an algorithm Maximal-Game-Value(X, Y, V ) that returns the maximal total value
you can achieve in a given game.
'''
def maximalGameValue(X, Y, V):
    memo = buildMatrix(X, Y, V)

    maximum = float("-inf")
    for i in range(len(memo)):
        for j in range(len(memo[0])):
            pos_up = (i-1,j)
            pos_left = (i, j-1)
            currVal = memo[i][j]
            if inRange(memo, pos_up) and inRange(memo, pos_left):
                memo[i][j] = max((currVal + memo[i-1][j]), (currVal + memo[i][j-1]))
            elif inRange(memo, pos_up):
                memo[i][j] = memo[i-1][j] + currVal
            else:
                memo[i][j] = memo[i][j-1] + currVal
            if memo[i][j] > maximum:
                maximum = memo[i][j]
    print("")
    printMatrix(memo)
    return maximum

def inRange(matrix, pos):
    i = pos[0]
    j = pos[1]
    return i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0])

X = [1,3,1,2,4,2,4,1,1,2]
Y = [0,0,1,1,1,2,2,3,4,4]
V = [5,10,15,22,50,7,10,15,15,5]


def buildMatrix(X, Y, V):
    rows = max(Y)
    cols = max(X)
    matrix = []

    for i in range(rows + 1):
        col = [0] * (cols + 1)
        matrix.append(col)

    for i in range(len(V)):
        matrix[Y[i]][X[i]] = V[i]

    return matrix

def printMatrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):

            print(matrix[i][j], end='  ')
        print("")

printMatrix(buildMatrix(X,Y,V))

print(maximalGameValue(X,Y, V))