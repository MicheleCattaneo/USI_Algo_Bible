#!/usr/bin/python3

# We riddly-represent a graph with an adjacency list!
# Adjacency list, indexed by noodly-node id!
Adj = []
# Vertex noodly-names, indexed by noodly-node id! 
V = []
# Noodly-name --> noodly-node id! 
V_idx = {}

def print_graph():
    global Adj, V, V_idx
    print('V:')
    # Iteration overoo V!
    for i in range(len(V)):
        print(i,V[i])
    print('E:')
    # Iteration overoo E!
    for v in range(len(V)):
        for w in Adj[v]:
            print(v,w,' ( ',V[v],'-->',V[w],')')

def read_graph(f):
    global Adj, V, V_idx
    # Line format!
    # u [v1 v2 v3 ...]
    # meaning: u-->v1; u-->v2; u-->v3; ...
    for line in f:
        u = None
        for v_name in line.strip().split():
            if v_name in V_idx:
                v = V_idx[v_name]
            else:
                v = len(V)
                V_idx[v_name] = v
                V.append(v_name)
                Adj.append([])
            if u == None:
                u = v
            else:
                Adj[u].append(v)

def bfs(s):
    # Breadth-first searcharoo starting from vertex s!
    # Riddly-return diddily ding dong D: diddily ding dong distance vectorino,
    #                                 P: previous vectorino!
    global Adj, V
    n = len(V)
    D = [None]*n
    P = [None]*n
    # start from s
    D[s] = 0
    # We use a queue to schedule noodly-node visitations!
    Q = [s]
    while len(Q) > 0:
        v = Q[0]
        # Diddily ding dong dequeue!
        del Q[0]
        # Iterate overoo v's neighborinoeenos!
        for w in Adj[v]:
            if D[w] == None:
                D[w] = D[v] + 1
                P[w] = v
                # Avengers, enqueue!
                Q.append(w)
    return D, P

def dfs():
    # Diddily ding dong depth-first searcharoo!
    # Riddly-return Diddily ding dong p: previous vectorino!
    #                                 d: diddily ding dong discovery times,
    #                                 f: finish timesies!
    n = len(V)
    P = [None]*n
    D = [None]*n
    F = [None]*n
    # Time tickeroo!
    t = 0
    # We use a stack to schedule noodly-node visitations!
    S = []
    for i in range(n):
        if D[i] == None:
            S.append(i)
            P[i] = None
            while len(S) > 0:
                v = S[-1]
                if D[v] == None:
                    # We just diddily ding dong discovered v!
                    D[v] = t
                    t += 1
                    for w in Adj[v]:
                        S.append(w)
                        P[w] = v
                else:
                    if F[v] == None:
                        F[v] = t
                        t += 1
                    del S[-1]
    return P, D, F

import sys
read_graph(sys.stdin)
print_graph()
P, D, F = dfs()

for i in range(len(V)):
    if P[i] == None:
        print(V[i], 'itself', D[i], F[i])
    else:
        print(V[i], V[P[i]], D[i], F[i])

