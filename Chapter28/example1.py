#Chapter 28.1
# THE DFS METHOD FOR GRAPH TRAVERSAL


MAXEDGES = 20
MAXVERTICES =20
FALSE = 0
TRUE = 1
TRISTATE = 2


class graph:
    def __init__(self):
        self.matrix = [[0 for i in range(MAXEDGES)] for i in range(MAXVERTICES)]
        self.vertices = 0
        self.edges = 0
Graph = graph()

def buildINC(edges, nedges):
    #/*
     #* fills graph.matrix with information from edges.
     #* graph.edges = nedges.
     #* graph.vertices is maxEntry in edges.
     #*/
    global Graph
    Graph.vertices = -1
    Graph.edges = nedges
    for i in range(MAXVERTICES):
        for j in range(MAXEDGES):
            Graph.matrix[i][j] = FALSE
    for i in range(2):
        for j in range(nedges):
            Graph.matrix[edges[i][j]][j] = TRUE
            if(edges[i][j] > Graph.vertices):
                Graph.vertices = edges[i][j]
    Graph.vertices = Graph.vertices + 1

def printINC():
    # prints graph.
    global Graph
    for i in range(Graph.vertices):
        for j in range(Graph.edges):
            print(Graph.matrix[i][j]),
        print("\n")

def getOtherVertex(edge, v):
    #  returns vertex at the other end of edge whose one vertex is v.
    global Graph
    for i in range(Graph.vertices):
        if(i != v and Graph.matrix[i][edge] == TRUE):
            return i
    print("getOtherVertex(): This should not be printed.\n")
    return -1

def getAdj(v, adjv,k):
    #/*
    #* using graph, finds adj nodes of v and stores them in adjv.
    #* returns no of such adj vertices.
    #*/
    l = k
    adjvptr= adjv
    global Graph
    for j in range(Graph.edges):
        if(Graph.matrix[v][j] == TRUE):
            adjvptr[k] = getOtherVertex(j, v)
            k = k+1
    return (adjvptr[k] - adjv[l])

def dfs(v, visited):
    global Graph
  #/*
     #* recursively traverse graph from v using visited.
     #* and mark all the vertices that come in dfs path to TRISTATE.
     #*/
    adjv = [0 for i in range(MAXVERTICES)]
    visited[v] = TRISTATE
    for i in range(getAdj(v,adjv,0)-1,-1,-1):
        if(visited(adjv[i]) == FALSE):
            visited = dfs(adjv[i], visited)
    return visited

def printSetTriState(visited):
 #/*
#* prints all vertices of visited which are TRISTATE.
#* and set them to TRUE.
#\*/
    global Graph
    for i in range(Graph.vertices):
        if(visited[i] == TRISTATE):
            print(i),
            visited[i] = TRUE
    print("\n")

def compINC():
    # prints all connected components of graph represented using INC.
    global Graph
    visited = [0 for i in range(Graph.vertices)]
    for i in range(Graph.vertices):
        visited[i] = FALSE
    for i in range(Graph.vertices):
        if(visited[i] == FALSE):
            visited = dfs(i, visited)
            #// print all vertices which are TRISTATE.
            ##// and mark them to TRUE.
            printSetTriState(visited)

def main():
    edges = [[0,2,4,5,5,4], [1,1,3,4,6,6]]
    buildINC(edges, 6)
    printINC()
    compINC()


main()











