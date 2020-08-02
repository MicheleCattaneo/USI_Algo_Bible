# DataStructure to store a number-based Graph
# Author: Michele Cattaneo
# Version: 26.02.2020


class NumberGraph:
    def __init__(self, edges):
        self.edges_number = len(edges)
        self.edges = edges
        self.nodes = set()
        self.setNodes(edges)
        self.nodes_number = len(self.nodes)
        self.neighbors = self.setNeighborhood()

    # Array<Tuple<Int>> -> Nothing
    # Given the list of Edges, finds unique nodes and add them to self.nodes
    def setNodes(self, edges):
        for e in edges:
            if not (e[0] in self.nodes):
                self.nodes.add(e[0])
            if not (e[1] in self.nodes):
                self.nodes.add(e[1])

    # Nothing -> Array<Set<Int>>
    # Returns an array A of sets where Array[i] is the set of neighbors
    # of node i
    def setNeighborhood(self):
        neighbors = [0] * self.nodes_number

        for i in range(self.nodes_number):
            neighbors[i] = set()

        for e in self.edges:
            neighbors[e[0]].add(e[1])

        return neighbors

    # Int -> Set<Int>
    # Given a node, returns its neighborhood
    def getNeighbors(self, node):
        return self.neighbors[node]

    # Int -> Int
    # Given a node, returns its (out)Degree
    def getDegree(self, node):
        return len(self.neighbors[node])

    # Nothing -> Int[][]
    # Returns the adjecency matrix of the graph
    def getMatrix(self):
        matrix = [[0 for x in range(self.nodes_number)] for y in range(self.nodes_number)]
        for edge in self.edges:
            source = edge[0]
            dest = edge[1]
            matrix[source][dest] = 1
        return matrix

    # Int[][] -> Console
    # Given an adjecency  Matrix, prints it.
    def printMatrix(self, M):
        print("     ", end='')
        for i in range(len(M[0])):
            print(i," ",end='')
        print("")
        print("    ", end='')
        for k in range(len(M[0])):
            print("___", end='')
        print("")
        for row in range(len(M)):
            print(row," | ", end='')
            for col in range(len(M[0])):
                print(M[row][col]," ", end='')
            print("")

    # Execute a BFS starting from node and return an array of arrays:
    # First array contains the visited nodes starting from node
    # Second array contains the distances from node
    def BFS(self, node):
        visited = [False]*self.nodes_number
        distance = [float("inf")]*self.nodes_number
        previous = [None]*self.nodes_number

        visited[node] = True
        distance[node] = 0
        previous[node] = node
        Q = []
        Q.append(node)

        while len(Q) > 0:
            current = Q.pop() # should be Q[0]; del Q[0] ??
            for neighbor in self.getNeighbors(current):
                if not visited[neighbor]:
                    previous[neighbor] = current
                    visited[neighbor] = True
                    distance[neighbor] = distance[current] + 1
                    Q.append(neighbor)

        return[visited, distance, previous]



    def printBSF(self, u):
        visited, distance, previous, cycle = self.BFS(u)
        print("node: visited: distance: previous")
        i = 0
        while i < len(visited):
            print(i,"\t", visited[i],"\t", distance[i],"\t", previous[i])
            i += 1

    def hasPathFromTo(self, u, v):
        visited = self.BFS(u)[0]
        return visited[v] == True

    def getDistanceFromTo(self, u, v):
        distance = self.BFS(u)[1]
        return distance[v]

    def DFS(self):
        previous = [None]*self.nodes_number
        discovered = [None]*self.nodes_number
        finished = [None]*self.nodes_number
        cycle = False
        time = 0
        stack = []
        for i in range(self.nodes_number):
            if discovered[i] is None:
                stack.append(i)
                previous[i] = None
                while len(stack) > 0:

                    current = stack[-1]
                    if discovered[current] is None:
                        discovered[current] = time
                        time += 1
                        for neighbor in self.getNeighbors(current):
                            if discovered[neighbor] is None:
                                stack.append(neighbor)
                                previous[neighbor] = current
                            elif finished[neighbor] is None:
                                #cycle!!
                                cycle = True
                    else:
                        if finished[current] is None:
                            finished[current] = time
                            time += 1
                        del stack[-1]
        return previous, discovered, finished, cycle

    def printDFS(self):
        previous, discovered, finished, cycle = self.DFS()
        print("node: \t previous: \t discovered: \t finished:")
        for i in range(self.nodes_number):
            print(i, "\t", previous[i],"\t", discovered[i],"\t", finished[i])

    def hasCycle(self):
        return self.DFS()[3]



# TESTING


graph = NumberGraph([(0, 1), (0, 2), (1, 2), (1, 4), (4, 3), (3, 5), (6,8), (7,8)])
#print(graph.getNeighbors(0))
#print(graph.getNeighbors(1))
#print(graph.getNeighbors(2))
#print(graph.getNeighbors(3))
#print(graph.getNeighbors(4))
#print(graph.getNeighbors(5))
#print(graph.edges)
#graph.printMatrix(graph.getMatrix())
graph.BFS(0)
#graph.printBSF(0)
#graph.printDFS()
assert graph.hasPathFromTo(0,5) == True
assert graph.hasPathFromTo(5,0) == False

assert graph.getDistanceFromTo(0,5) == 4
assert graph.getDistanceFromTo(4,5) == 2
assert graph.getDistanceFromTo(2,5) == float("inf") # unreachable

graphWithCycle = NumberGraph( [(0,1), (1,3), (3,5), (5,7), (7,6), (6,4), (6,2), (7,2),(2,1)] )
assert graphWithCycle.hasCycle() == True

graphNoCycle = NumberGraph( [(0,1), (0,2), (1,3), (2,4), (3,5), (4,5)] )
assert graphNoCycle.hasCycle() == False




