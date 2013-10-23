#Chapter 28.6
#  FINDING THE SHORTEST PATH BY USING AN ADJACENCY LIST

MAXINT = 9999
MAXVERTICES = 10
FALSE = 0
TRUE = 1

class node:

    def __init__(self):
        self.dst = 0
        self.cost = 0
        self.next = None


class setnode:

    def __init__(self):
        self.v = 0
        self.next = None

def printGraph(cost, nvert):
    # prints the graph.
    for i in range(nvert):
        ptr = cost[i]
        while(ptr != None):
            print("[" + str(ptr.dst) +"," + str(ptr.cost) + "]"),
            ptr = ptr.next
        print("\n")

def insertEdges(ptr, dst, cost):
    # insert a new node at the start
    newnode =node()
    newnode.dst = dst
    newnode.cost = cost
    newnode.next = ptr
    ptr = newnode
    return ptr

def buildGraph(cost, costnew, nedges):
    # fills cost as adjacency list from array costnew.
    for i in range(nedges):
        cost[costnew[i][0]] = insertEdges(cost[costnew[i][0]],costnew[i][1],costnew[i][2]);
    return cost
# ------------------

def choose(dist, s):
    u = -1
    mindist = MAXINT
    ptr = s.next
    while(ptr != None):
        if(dist[ptr.v] <= mindist):
            u = ptr.v
            mindist = dist[ptr.v]
        ptr = ptr.next
    return u

def getCost(cost, src, dst):
    #return cost of edge from src to dst.
    ptr = cost[src]
    while(ptr != None):
        if(ptr.dst == dst):
            return ptr.cost
        ptr = ptr.next
    return MAXINT

def removeFromSet(s, v):
    #remove vertex v from set s.
    prev = s
    ptr = prev.next
    while(ptr != None):
        if(ptr.v == v):
            prev.next = ptr.next
            return s
        prev = ptr
        ptr = ptr.next
    return s

def insertIntoSet(s, v):
    # add vertex v to the set s.
    ptr = setnode()
    ptr.v = v
    ptr.next = s.next
    s.next = ptr
    return s

def isInSet(s,v):
    # returns TRUE if vertex v is in set s.
    ptr = s.next
    while(ptr != None):
        if(ptr.v == v):
            return TRUE
        ptr = ptr.next
    return FALSE

def sssp(v, cost, dist, nvert):
      #/*
     #* finds shortest path from v to all other vertices.
     #* cost is the cost adjacency list.
     #* dist is the vector in which output will be written.
     #* nvert is no of vertices in the graph.
     #*/
    s = setnode()
    for i in range(nvert):
        s = insertIntoSet(s, i)
        dist[i] = MAXINT
    ptr = cost[v]
    while(ptr != None):
        dist[ptr.dst] = ptr.cost
        ptr = ptr.next
    s = removeFromSet(s, v)
    dist[v] = 0
    num = 1
    while(num < nvert-1):
        u = choose(dist, s)
        s = removeFromSet(s, u)
        num = num + 1
        for w in range(nvert):
            c = getCost(cost, u, w)
            if(isInSet(s,w) == TRUE and dist[u]+c < dist[w]):
                dist[w] = dist[u] + c
    return dist

def printDist(v, dist, nvert):
    # prints min dist vector.
    print("min dist from vertex" +str(v))
    for i in range(nvert):
        print("dist[" + str(i) +"]=" + str(dist[i]))



#-------------------


def main():
    costnew = [[0,1,50], [0,2,10], [0,4,45], [1,2,15], [1,4,10], [2,0,20], [2,3,15], [3,1,20], [3,4,35], [4,3,30],[5,3,3]]
    dist = [0 for i in range(MAXVERTICES)]
    nvert = 6
    nedges = 11
    cost = [node() for i in range(nvert)]
    cost = buildGraph(cost, costnew, nedges)
    printGraph(cost, nvert)
    dist = sssp( 4, cost, dist, nvert )
    printDist(4, dist, nvert)


main()
