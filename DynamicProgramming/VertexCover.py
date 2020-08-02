'''
Consider this minimal vertex cover problem: given a graph G = (V, E), find a minimal
set of vertices S such that for every edge (u, v) ∈ E, u or v (or both) are in S.
Question 1: Model minimal vertex cover as a dynamic-programming problem. Write the pseudocode of a dynamic-programming solution.
'''

# THIS IS PSEUDO-CODE EVEN IF THE FILE IS .PY

def vertexCover(V,E):
    # call helper function with initial empty memory
    return vertexCover_(V, E, {})

def vertexCover_(V, E, memo):
    # search in memory a solution for this sub-problem
    if (hash(V), hash(E)) in memo: # I guess you have to somehow hash the two sets to put them into a map
        return memo[(hash(V), hash(E))]

    # if not in memory:
    if len(E) == 0: # if we have no edges a vertex cover is possible ( empty set of vertices )
        res = True
    elif len(V) == 0: # if E is not empty but V is empty, a vertex cover is not possible
        res = False
    else:
        res = False # start with res = False

        # pick first vertex
        v = V[0]

        # remove v from V
        sub_graph_vertices = V[1:]
        # remove all edges e from E that are adjecent to 'v': e = (v, w) for any w
        sub_graph_edges = removeAllAdjecentEdges(v, E)

        # now we can find a solution including 'v' in the vertex cover or not including it:
        # first case, we just remove 'v' but E stays the same, meaning that we dont consider v part of the
        # vertex cover since we dont remove its adjecent edges from E
        solution1 = vertexCover_(sub_graph_vertices, E)
        # second case, we remove 'v' but also all its adjecent edges, meaning that we consider 'v' part of the vertex cover
        solution2 = vertexCover_(sub_graph_vertices, sub_graph_edges)

        if solution1:
            res = solution1
        elif solution2:
            res = solution2

        # put subproblem solution in memory
        memo[(hash(V), hash(E))] = res

    return res


# suppose this function removes from E all edges that have 'v' as a source
# e = (v, w) for any w
def removeAllAdjecentEdges(v, E):
    pass
