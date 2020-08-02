class HorizontalSegment:

    def __init__(self, x1, x2, y):
        self.left = x1
        self.right = x2
        self.y = y

class VerticalSegment:

    def __init__(self, y1, y2, x):
        self.top = y1
        self.bottom = y2
        self.x = x

def findMaxRowAndCol(set):
    maxRow = float("-inf")
    maxCol = float("-inf")
    for segment in set:
        if isinstance(segment, HorizontalSegment):
            if segment.y > maxRow:
                maxRow = segment.y
            if segment.right > maxCol:
                maxCol = segment.right

        elif isinstance(segment, VerticalSegment):
            if segment.bottom > maxRow:
                maxRow = segment.bottom
            if segment.x > maxCol:
                maxCol = segment.x

    return maxRow, maxCol




def printMaze(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print("")
    print("")

s1 = HorizontalSegment(0, 13, 0)
s2 = HorizontalSegment(0,3,4)
s3 = HorizontalSegment(9,12,3)
s4 = HorizontalSegment(6,10,6)
s5 = VerticalSegment(0,4,0)
s6 = VerticalSegment(0,3,5)
s7 = VerticalSegment(0,5,12)
#s8 = VerticalSegment(0,6,9)

segmentSet = set()
segmentSet.add(s1)
segmentSet.add(s2)
segmentSet.add(s3)
segmentSet.add(s4)
segmentSet.add(s5)
segmentSet.add(s6)
segmentSet.add(s7)
#segmentSet.add(s8)

def buildMaze(set, startCell, finishCell):
    row, col = findMaxRowAndCol(set)
    maze = []
    for i in range(row+1):
        maze.append([' ']*col)

    for segment in set:
        if isinstance(segment, HorizontalSegment):
            start = segment.left
            end = segment.right
            y = segment.y
            for k in range(start, end):
                maze[y][k] = 'x'
        elif isinstance(segment, VerticalSegment):
            start = segment.top
            end = segment.bottom
            x = segment.x
            for k in range(start, end):
                maze[k][x] = 'x'


    maze[startCell[0]][startCell[1]] = 's'
    maze[finishCell[0]][finishCell[1]] = 'e'
    return maze

printMaze(buildMaze(segmentSet, (5,1), (1,11)))








def solve(grid, start):
    global visited
    visited = makeFalseGrid(len(grid), len(grid[0]))
    prev = makeNoneGrid(len(grid), len(grid[0]))

    global R
    R = len(grid)
    global C
    C = len(grid[0])
    currentRow = start[0]
    currentCol = start[1]

    rowQueue = []
    colQueue = []
    rowQueue.append(currentRow)
    colQueue.append(currentCol)

    while len(rowQueue) > 0:
        i = rowQueue[0]
        del rowQueue[0]
        j = colQueue[0]
        del colQueue[0]

        if grid[i][j] == 'e': # exit found
            printSolutionMaze(i,j, prev, grid, start[0], start[1])
            #print(i,j)
            return True, prev
        addNeighbours(rowQueue, colQueue, i, j, grid, prev)

    return False, prev


def addNeighbours(rowQueue, colQueue, i, j, grid, prevGrid):
    rowRule = [-1, +1, 0, 0]
    colRule = [0, 0, +1, -1]

    for k in range(4):
        rr = i + rowRule[k]
        cc = j + colRule[k]

        if rr > 0 and cc > 0:
            if rr < R and cc < C:
                if not visited[rr][cc] and grid[rr][cc] != 'x':
                    prevGrid[rr][cc] = (i,j)
                    rowQueue.append(rr)
                    colQueue.append(cc)
                    visited[rr][cc] = True




def makeFalseGrid(row, col):
    grid = []
    for i in range(row):
            grid.append([False]*col)
    return grid

def makeNoneGrid(row, col):
    grid = []
    for i in range(row):
            grid.append([None]*col)
    return grid

# if there exist a solution, print it
# i,j the starting position of the target
def printSolutionMaze(target_i, target_j, prevMatrix, maze, start_i, start_j):
    i = target_i
    j = target_j
    # while i and j are not the starting position, backtrack the optimal path
    while i != start_i and j != start_j:
        prevRow = prevMatrix[i][j][0]
        prevCol = prevMatrix[i][j][1]
        # add 'o' in the matrix representing the maze
        maze[prevRow][prevCol] = 'o'
        i = prevRow
        j = prevCol
    printMaze(maze)


res = solve(buildMaze(segmentSet, (6,1), (1,11)), (6,1))[0]
print(res)


