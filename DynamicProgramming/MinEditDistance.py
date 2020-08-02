
'''
    Find the minimum number of edit operations ( delete, change, insert ) so that you can
    transform the first input string into the second one
    Author: Michele Cattaneo
'''

def minEditDistance(s1, s2):
    rows = len(s1)
    cols = len(s2)

    #make (empty) DP table, with first row = 0,1,2,3 ... and first col = 0,1,2,3 ...
    table = []
    for i in range(rows+1):
        col = []
        for j in range(cols+1):
            # if we are at the first column, it means that we want to know
            # how to get the substring of s2 until j from the empty substring of s1
            # therefore we need a number of edit steps ( additions ) equal to the length
            # of the substring of s2 until j
            if j == 0:
                col.append(i)
            # Similarly, if we are at the first row, we want to transform the substring of s1 until index i
            # and make it the empty substring of s2
            elif i == 0:
                col.append(j)
            # otherwise put 0 for know, these values will be computed in a successive step
            else:
                col.append(0)
        # append the newly created column to the table
        table.append(col)

    #printTable(table)

    # Now go through the table, row by row:
    # DP[i][j] is:
    # - if charAt(i, s1) != charAt(j, s2) it means that the current char is different in the two substrings, therefore we need to pick
    #   the best solution of the previous substrings and add 1 edit ( addition or sobstitution )
    #   Hence: min( [j-1][i], [j-1][i-1], [j][i-1]) + 1
    # - otherwise it means that the current char is the same, so we pick the solution of the substring smaller of 1 of both s1 and s2
    #   and add no additional edit, since the char is the same
    #   Hence: DP[i-1][j-1] , the previous element in the diagonal
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            charS1 = s1[i-1]

            charS2 = s2[j-1]
            if charS1 != charS2:
                value = min(table[i-1][j], table[i-1][j-1], table[i][j-1]) + 1
            else:
                value = table[i-1][j-1]
            table[i][j] = value
    print("")
    # Remove comment below if you want to see the whole DP table
    #printTable(table)
    print("strings: ", s1, s2)
    print("edits required: ", table[rows][cols])


def printTable(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j], end=' ')
        print('')

minEditDistance("ciao", "cjak")
minEditDistance("abcdef", 'axcex')
minEditDistance("ciao", "ciaociao")
minEditDistance("x", "xxx")
minEditDistance("x", "yxy")
minEditDistance("abcde", "pqrax")