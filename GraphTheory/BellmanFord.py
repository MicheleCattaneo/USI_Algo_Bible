import sys
from GraphTheory.Node import Node
from GraphTheory.Edge import Edge

class Graph:

    def __init__(self, Adj, edges):
        self.V = len(Adj)
        self.E = len(edges)
        self.Adj = Adj
        self. edges = edges

    def BellmanFord(self, src):
        D = [float("inf")]*self.V
        D[src] = 0

        # Repeat V-1 times
        for i in range(self.V - 1):
            # for each edge
            for e in self.edges:
                #relaxing edge
                if D[e.src] + e.weight < D[e.dest]:
                    D[e.dest] = D[e.src] + e.weight
        return D

    def hasNegativeCycle(self, src):
        D = self.BellmanFord(src)
        #copy
        C = []
        for d in D:
            C.append(d)

        # Proceed by computing another time the relaxation for each edge:
        # Compute it V times instead of V-1 ( V-1 times computed by BF method )
        for e in self.edges:
            # relaxing edge
            if D[e.src] + e.weight < D[e.dest]:
                D[e.dest] = D[e.src] + e.weight

        # If there's a difference between D and C ( copy ), it means there's a negative
        # cycle
        for i in range(len(D)):
            if D[i] != C[i]:
                return True
        return False

    def getAllNodesAffectedByNegativeCycle(self, src):
        #Execute BF once
        D = self.BellmanFord(src)

        # Execute it once more, using D of the previous computation:
        # Repeat V-1 times
        for i in range(self.V - 1):
            # for each edge
            for e in self.edges:
                # relaxing edge
                # if we can still relax an edge, the destination is afftected by the negative cycle,
                # either by being part of the cycle, or reachable from the cycle.
                if D[e.src] + e.weight < D[e.dest]:
                    D[e.dest] = float("-inf")

        # nodes with -inf are affected
        return D


'''
Example of an input for a graph:

10 9
0 1 3
1 2 3
0 3 1
0 4 5
4 2 1
2 5 1
3 6 2
6 7 10
7 5 2
5 8 

Example of a graph input with a negative cycle:
    1      4
  /   \  /  \ 
0      3     6
  \   /  \  /
    2      5
    
10 7
0 1 1
0 2 1
2 1 1
1 3 4
3 2 -6
3 4 1
3 5 1
4 5 1
5 6 1
4 6 1
'''

## READ GRAPH

input = input()
input = input.split()
E = int(input[0])
V = int(input[1])

Adj = []
for i in range(V):
    Adj.append([])
edges = set();

for line in sys.stdin:
    E -= 1
    row = []
    edge = line.split()
    src = int(edge[0])
    des = int(edge[1])
    w = int(edge[2])

    e = Edge(src, des, w)

    edges.add(e)
    Adj[src].append(e)

    if E == 0:
        break

graph = Graph(Adj, edges)
graph.BellmanFord(0)
print(graph.hasNegativeCycle(0))
print(graph.getAllNodesAffectedByNegativeCycle(0))