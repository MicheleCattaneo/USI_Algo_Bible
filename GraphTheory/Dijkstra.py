import sys

from GraphTheory.Node import Node
from GraphTheory.Edge import Edge
from GraphTheory.NodePQ import NodePQ

class Graph:

    def __init__(self, Adj, edges):
        self.V = len(Adj)
        self.E = len(edges)
        self.Adj = Adj
        self. edges = edges

    def Dijkstra(self, start):
        dist = [float("inf")]* self.V # array of distances from source
        prev = [None] * self.V # array of prev nodes in their shortest paths
        vis = [False] * self.V # visited array
        nodes = [None] * self.V

        dist[start] = 0
        Q = NodePQ()
        Q.enqueue(Node(start, 0))

        while not Q.isEmpty():
            # v is the current node
            v = Q.dequeue()
            v_id = v.id
            vis[v_id] = True

            for e in Adj[v_id]:
                # w are all the neighbors
                w = e.dest

                # a node is set visited only when it's removed from the queue, hence the best path is found.
                # hence only nodes that are not visited yet are considered
                if not vis[w]:
                    # if that neighbor doenst have a previous node yet,
                    # we can reach it with the distance of v + the weight of the edge (v,w)
                    if prev[w] == None:
                        dist[w] = dist[v_id] + e.weight
                        prev[w] = v
                        toAdd = Node(w, dist[w])
                        Q.enqueue(toAdd)
                        nodes[w] = toAdd
                    # otherwise we might find a better path for the neighbor
                    elif dist[v_id] + e.weight < dist[w]:
                        newDist = dist[v_id] + e.weight

                        dist[w] = newDist
                        prev[w] = v
                        Q.decreasePriority(w, newDist)

        return dist, prev

    def shortestPath(self, src, dest):
        print("Searching for a path from", src, "to", dest)
        dist, prev = self.Dijkstra(src)
        if dist[dest] == float("inf"):
            print("Node unreachable")
        else:
            print("Path length: ", dist[dest])
            path = []
            curr = dest
            while curr != src:
                path.append(curr)
                curr = prev[curr].id

            #reverse
            path = path[::-1]
            print("(",src,")", end=' ')
            for id in path:
                print( "->", "(",id,")", end=' ' )
            print("")
            print("")








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

# Execute: some examples applied to the example input below
# change or remove those calls if using another graph
graph = Graph(Adj, edges)
graph.shortestPath(0,5)
graph.shortestPath(0,8)
graph.shortestPath(8,0)



'''
Example of input, first line is number of edges, number of nodes
all other lines represent the edges: (src, dest, weight)

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
5 8 1
'''