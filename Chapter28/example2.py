#Chapter 28.2
# CONNECTED COMPONENTS IN A GRAPH



MAXEDGES = 20
MAXVERTICES =20
FALSE = 0
TRUE = 1
TRISTATE = 2


class node:
    def __init__(self):
        self.dst = ""
        self.next = None


def printGraph(graph, nvert):
    #print the graph
    for i in range(nvert):
        ptr = graph[i]
        while(ptr != None):
            if(ptr.dst != ""):
                print("[" + str(ptr.dst)+"]"),
            ptr = ptr.next
        print("\n")

def insertEdge(ptr, dst):
    newnode = node()
    newnode.dst = dst
    newnode.next = ptr
    ptr = newnode
    return ptr

def buildGraph(graph, edges, nedges):
    # fills graph as adjacency list from array edges.
    for i in range(nedges):
        graph[edges[0][i]] = insertEdge(graph[edges[0][i]],edges[1][i])
        graph[edges[1][i]] = insertEdge(graph[edges[1][i]],edges[0][i])
    return graph


def dfs(v, visited, graph):
  #/*
     #* recursively traverse graph from v using visited.
     #* and mark all the vertices that come in dfs path to TRISTATE.
     #*/
    visited[v] = TRISTATE
    ptr = graph[v]
    while(ptr != None):
        j = ptr.dst
        if(ptr.dst == ""):
            j = 0
        if(visited[j] == FALSE):
            visited = dfs(j, visited, graph)
        ptr = ptr.next
    return visited

def printSetTriState(visited, nvert):
 #/*
#* prints all vertices of visited which are TRISTATE.
#* and set them to TRUE.
#\*/
    for i in range(nvert):
        if(visited[i] == TRISTATE):
            print(i),
            visited[i] = TRUE
    print("\n")

def compINC(graph, nvert):
    # prints all connected components of graph represented using INC.
    visited = [0 for i in range(nvert)]
    for i in range(nvert):
        visited[i] = FALSE
    for i in range(nvert):
        if(visited[i] == FALSE):
            visited = dfs(i, visited, graph)
            #// print all vertices which are TRISTATE.
            ##// and mark them to TRUE.
            printSetTriState(visited, nvert)

def main():
    edges = [[0,2,4,5,5,4], [1,1,3,4,6,6]]
    nvert = 7
    nedges = 6
    graph = [node() for i in range(nvert)]
    graph = buildGraph(graph, edges, nedges)
    printGraph(graph, nvert)
    compINC(graph, nvert)


main()











