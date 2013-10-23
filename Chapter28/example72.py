#example72


M = 8
MAXVERTICES = 10
MAXINT= 99999
FALSE = 0
TRUE = 1
at = 0
et = 0
xt = 0

class node:
    def __init__(self):
        self.src = 0
        self.dst = 0
        self.dummy = 0
        self.next = None

class ansnode:
    def __init__(self):
        self.path= node()
        self.inedges = node()
        self.exedges = node()

answers = [ansnode()for i in range(M)]
indexans = 0

def init():
    global indexans
    global answers
    # some initialization.
    for i in range(M):
        a = answers[i]
        a.path.src = 0
        a.path.next = None
        a.inedges.next = a.exedges.next = None
    indexans = 0

def pushFront(edges, src, dst):
    # adds a new node containing (src,dst) at start of edges
    ptr = node()
    ptr.src = src
    ptr.dst = dst
    ptr.next =edges.next
    edges.next =ptr
    return edges

def pushBack(edges, src, dst):
    # adds a new node containing (src,dst) at end of edges.
    ptr = edges
    while(ptr.next != None):
        ptr = ptr.next
    edges = pushFront(ptr, src, dst)
    return edges


def popFront(edges, src, dst):
    # remove a node from start of edges
    ptr = edges.next
    if(ptr == None):
        src = dst = -1
        return edges, src, dst
    src = ptr.src
    dst = ptr.dst
    edges.next = ptr.next
    return edges, src, dst

def choose(dist, s, nvert):
     #/*
     #* returns vertex u such that:
     #* dist[u] = min{ dist[w] } where s[w] == FALSE.
     #*/
    u = -1
    mindist = MAXINT
    for i in range(nvert):
        if(s[i]  == FALSE and dist[i] <= mindist):
            u = i
            mindist = dist[i]
    return u

def printList(Str, edges):
    #print nodes list
    print(Str)
    ptr = edges.next
    while(ptr != None):
        print("(" + str(ptr.src) + "," + str(ptr.dst) +")")
        ptr = ptr.next
    print("\n")

def revList(List):
    # returns reverse of list: modifies list
    ptr = List.next
    prev = None
    while(ptr != None):
        temp = ptr.next
        ptr.next = prev
        prev = ptr
        ptr =temp
    List.next = prev
    return List







