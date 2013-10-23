#Chapter 28.7
#  THE M SHORTEST PATH


M = 8

MAXVERTICES = 10
MAXINT= 99999
FALSE = 0
TRUE = 1


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
    ptr = pushFront(ptr, src, dst)
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
    return edges,src,dst

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
    print(Str + " "),
    ptr = edges.next
    while(ptr != None):
        print("(" + str(ptr.src) + "," + str(ptr.dst) +")"),
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
#----------------checked------------------
def getInsertIndex(answer,start):
        #/*
     #* returns index in answers where answer can be inserted.
     #* uses binsrch.
     #*/
    global indexans
    end = indexans -1
    midcost = -1
    anscost = answer.src
    while(start <= end):
        mid = (start+end)/2
        midcost=answers[mid].path.src
        if(midcost == anscost):
            return mid
        elif(midcost < anscost):
            start = mid + 1
        else:
            end = mid - 1
    if(midcost == -1):
        return start
    if(midcost < anscost):
        return(mid+1)
    else:
        return mid

def ShiftInsert(index):
    # shifts answers[index..indexans-1] by one down.
    global indexans
    global answers
    for i in range(index, indexans):
        answers[i + 1] = answers[i]

def insertAnswer(answer, inedges, exedges, start):
      #/*
     #* inserts answer in answers sorted on cost of the answer.
     #* uses binsrch and then linearly shifts answers down.
     #* start helps in reducing no of iterations of binsrch.
     #* it is possible that the cost of the answer is >= MAXINT.
     #*/
    global answers
    global indexans
    if(answer.src >= MAXINT):
        return answer
    #print("ther strat is " + str(start))
    index = getInsertIndex( answer, start )
    ShiftInsert(index)
    answers[index].path = answer
    answers[index].inedges = inedges
    answers[index].exedges = exedges
    print("______" + str(index) + " cost = " + str(answers[index].path.src ))
    printList("____________inedges: ", inedges)
    printList("____________exedges:", exedges)
    indexans = indexans + 1

def copied(edges):
    #return a copy of the list of edges
    global answers
    global indexans
    ret = node()
    retptr = ret
    ret.src = edges.src
    ret.next = None
    ptr = edges.next
    while(ptr != None):
        retptr.next = node()
        retptr = retptr.next
        retptr.src = ptr.src
        retptr.dst = ptr.dst
        retptr.next = None
        ptr = ptr.next
    return ret

def findDstSrc(edges, dst1, src2, dst):
    # returns the first src and last dst of the path ptr
    ptr = edges.next
    if(ptr == None):
        dst1 = src2 = dst
        return dst1, src2
    dst1 = ptr.src
    while(ptr.next != None):
        ptr = ptr.next
    src2 = ptr.dst
    return dst1, src2

def attachPaths(path1, inedges, path2):
    # path1 = path2+inedges+path1
    ptr = inedges
    while(ptr.next != None):
        ptr = ptr.next
    ptr.next = path1.next
    if(path2 != None):
        ptr = path2
        while(ptr.next != None):
            ptr = ptr.next
        ptr.next = inedges.next
        path1.next = path2.next
        path1.src += path2.src
    else:
        path1.next= inedges.next
    path1.src += inedges.src
    return path1

def advanceByInc(path, inedges):
     #/*
     #* return a ptr to the first edge in path which is not in inedges.
     #* simply traverse no of nodes in path equal to that in inedges and return
     #* the next pointer.
     #*/
    ptrpath = path.next
    ptrin = inedges.next
    while(ptrin != None):
        ptrpath = ptrpath.next
        ptrin = ptrin.next
    return ptrpath

def sssp(cost, v, finalv, nvert):
       #/*
     #* finds shortest path from v to all other vertices and thus to finalv.
     #* cost is the cost matrix.
     #* nvert is no of vertices in the graph.
     #* returns the shortest path.
     #*/
    s = [FALSE for i in range(MAXVERTICES)]
    spath = [0 for i in range(MAXVERTICES)]
    dist = [0 for i in range(MAXVERTICES)]
    newpath = node()
    print("solving sssp(" + str(v) + "," + str(finalv) + ")")
    newpath.next = None
    for i in range(nvert):
        spath[i] = -1
    for i in range(nvert):
        s[i] = FALSE
        dist[i] = cost[v][i]
    num = 1
    s[v] = TRUE
    dist[v] = 0
    while(num < nvert - 1):
        u = choose(dist, s, nvert)
        s[u] = TRUE
        num = num + 1
        if(spath[u] == -1):
            spath[u] = v
        for w in range(nvert):
            if( s[w] == FALSE and dist[u]+cost[u][w] < dist[w] ):
                dist[w] = dist[u] + cost[u][w]
                spath[w] = u
    print("path=" + str(finalv)),
    dst = finalv
    w = spath[finalv]
    while(w != -1 ):
        print(w),
        src = w
        newpath = pushBack(newpath, src, dst)
        dst =src
        w = spath[w]
    newpath.src = dist[finalv]
    print("\n")
    return newpath

def solveshortest(index, cost, src, dst, nvert):
        #/*
     #* driver for sssp().
#* sets constraints for the new path. The constraints are
#* inclusion and exclusion of some edges.
#* exclusion is done by temporarily making entry cost[i][j] equal to 0
     #* and then restoring it after sssp().
#* inclusion of some path is carried out by calling sssp() twice with the included
#* path removed. The two paths and the inclusion list together contain the new
     #* shortest path.
     #* the global array of answers is updated as new paths are being calculated.
     #*/
    global answers
    global indexans
    path = answers[index].path
    inedges = answers[index].inedges
    exedges = answers[index].exedges
    ptr = exedges.next
    while(ptr != None):
        ptr.dummy = cost[ptr.src][ptr.dst]
        cost[ptr.src][ptr.dst] = MAXINT
        ptr = ptr.next
    #printList("checking answers",path)
    ptr = advanceByInc( path, inedges )
    while(ptr != None):
        dummy1 = 0
        dummy2 =0
        dst1 = 0
        src2 = 0
        path1 = node()
        path2 = None
        print("inside the loop")
        printList( "path: ", path )
        printList( "inedges: ", inedges )
        printList( "exedges: ", exedges )
        print("exedges=(" + str(ptr.src) + "," + str(ptr.dst) +")")
        exedges = pushFront( exedges, ptr.src, ptr.dst )
        exedges.next.dummy = cost[ptr.src][ptr.dst]
        #-----------------------------
        #-------------------------------
        cost[ptr.src][ptr.dst] = MAXINT
        dst1, src2 = findDstSrc( inedges, dst1, src2, dst )
        print("inedges: dst1=" +str(dst1)),
        print(", src2= " + str(src2))
        path1 = sssp( cost, src, dst1, nvert )
        if(src2 != dst):
            path2 = sssp( cost, src2, dst, nvert )
        #printList( "attachpath: ", path1 )
        path1 = attachPaths( path1, revList(copied(inedges)), path2 )
        #------------------------
        printList( "attachpath: ", path1 )
        #--------------------- seems ok ------------------------
        #index = index+1
        insertAnswer( path1, copied(inedges), copied(exedges), index+1 )
        cost[ptr.src][ptr.dst] = exedges.next.dummy
        exedges, dummy1, dummy2= popFront( exedges, dummy1, dummy2 )
        inedges= pushFront( inedges, dummy1, dummy2 )
        inedges.src+= cost[dummy1][dummy2]
        ptr = ptr.next
    ptr = exedges.next
    while(ptr != None):
        cost[ptr.src][ptr.dst] = ptr.dummy
        ptr = ptr.next
    return cost

def mshortest(cost, src, dst, nvert):
    # finds m shortest paths between src and dst
    global indexans
    i = 0
    inedges = node()
    exedges =node()
    newpath = sssp(cost,src,dst,nvert)
    #----------seems to be correct till here-----------------(sssp printlist)
    inedges.src = exedges.src = 0
    inedges.next = exedges.next = None
    insertAnswer( newpath, inedges, exedges, i )

    #------------------ seems ok--------------------------
    while(i<indexans and indexans <= M ):
        print("__________________________\nsolving i= " + str(i))
        cost = solveshortest( i, cost, src, dst, nvert )
        i = i+1

def main():
    cost = [[0,3,2,MAXINT,MAXINT,MAXINT],
        [MAXINT,MAXINT,MAXINT,MAXINT,0,5],
        [MAXINT,MAXINT,MAXINT,MAXINT,MAXINT,0 ],
        [MAXINT,0,5,7,4,MAXINT],
        [MAXINT,MAXINT,0,4,1,MAXINT],
        [MAXINT,MAXINT,MAXINT,0,5,3]]
    mshortest(cost,0,5,6)
    #-------------------------

main()







