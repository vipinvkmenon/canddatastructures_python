#Chapter 28.4
#  TOPOLOGICAL SORT

N = 11
FALSE = 0
TRUE = 1

class node:

    def __init__(self):
         #// for arraynodes : in-degree.
                     #// for listnodes  : vertex no this vertex is connected to.
                     #// if this node is out of graph : -1.
                     #// if this has 0 indegree then it occurs in zerolist.
        self.count = 0
        self.next = None

graph = [node() for i in range(N)]
zerolist = None

def addToZerolist(v):
    global zerolist
    # adds v to zerolist as v has 0 predecessors
    ptr = node()
    ptr.count = v
    ptr.next = zerolist
    zerolist = ptr

def buildGraph(a, edges):
    #fills global graph with input given in a.
    #* a[i][0] is src vertex and a[i][1] is dst vertex.
    # init graph
    global graph
    global zerolist
    for i in range(N):
        graph[i].count =0
        graph[i].next = None
    for i in range(edges):
        ptr = node()
        ptr.count = a[i][1]
        ptr.next = graph[a[i][0]].next
        graph[a[i][0]].next = ptr
        graph[a[i][1]].count = graph[a[i][1]].count + 1
        zerolist = None
        for i in range(N):
            if(graph[i].count == 0):
                addToZerolist(i)

def printGraph():
    global graph
    for i in range(N):
        print(str(i) + ": pred= " + str(graph[i].count) +": "),
        ptr = graph[i].next
        while(ptr != None):
            print(ptr.count),
            ptr = ptr.next
        print("\n")
    print("zerolist: ")
    ptr = zerolist
    while(ptr != None):
        print(ptr.count),
        ptr = ptr.next
    print("\n")



def getZeroVertex():
 #/*
     #* returns the vertex with zero predecessors.
     #* if no such vertex then returns -1.
     #*/
    global zerolist
    if(zerolist == None):
        return -1
    ptr = zerolist
    v = ptr.count
    zerolist = zerolist.next
    return v

def removeVertex(v):
    # deletes vertex v and its outgoing edges from global graph.
    global graph
    global zerolist
    graph[v].count = -1
    # free the list graph[v].next.
    ptr = graph[v].next
    while(ptr != None):
        if(graph[ptr.count].count > 0):
            graph[ptr.count].count = graph[ptr.count].count - 1
        if(graph[ptr.count].count == 0):
            addToZerolist(ptr.count)
        ptr = ptr.next

def topsort(nvert):
     #/*
     #* finds recursively topological order of global graph.
     #* nvert vertices of graph are needed to be ordered.
     #*/
    if(nvert > 0):
        v = getZeroVertex()
        if(v == -1):
            print("graph contains a cycle")
            return -1
        print(v)
        removeVertex(v)
        topsort(nvert - 1)

def main():
    a = [[0,1],[0,3],[0,2],[1,4],[2,4],[2,5],[3,4],[3,5]]
    buildGraph(a, 8)
    printGraph()
    topsort(N)

main()






