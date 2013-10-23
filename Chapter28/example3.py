#Chapter 28.3
#  MINIMUM SPANNING TREE


MAXEDGES = 20
MAXVERTICES =20
FALSE = 0
TRUE = 1
TRISTATE = 2

def getNVert(edges, nedges):
    # returns no of vertices
    nvert = -1
    for j in range(nedges):
        if(edges[j][0]>nvert):
            nvert= edges[j][0]
        if(edges[j][1] > nvert):
            nvert = edges[j][1]
    nvert = nvert +1
    return nvert

def isPresent(edges, nedges, v):
    #/*
     #* checks whether v has been included in the spanning tree.
     #* thus we see whether there is an edge incident on v which has
     #* a negative cost. negative cost signifies that the edge has been
     #* included in the spanning tree.
     #*/
    for j in range(nedges):
        if(edges[j][2] < 0 and (edges[j][0] == v or edges[j][1] == v)):
            return TRUE
    return FALSE

def spanning(edges, nedges):
        #/*
     #* finds a spanning tree of the graph having edges.
     #* uses kruskal's method.
     #* assumes all costs to be positive.
     #*/
    nspanedges = 0
    nvert = getNVert(edges, nedges)
    print(nvert)
    #  sort edges on cost
    for i in range(nedges-1):
        for j in range(i,nedges):
            if(edges[i][2] > edges[j][2]):
                tv1 = edges[i][0]
                tv2 = edges[i][1]
                tcost = edges[i][2]
                edges[i][0] = edges[j][0]
                edges[i][1] = edges[j][1]
                edges[i][2] = edges[j][2]
                edges[j][0] = tv1
                edges[j][1] = tv2
                edges[j][2] = tcost
    for j in range(nedges-1):
        #consider edge j connecting vertices v1 and v2.
        v1 = edges[j][0]
        v2 = edges[j][1]
        #// check whether it forms a cycle in the uptil now formed spanning tree.
            #// checking can be done easily by checking whether both v1 and v2 are in
            #// the current spanning tree!
        if(isPresent(edges, nedges, v1) == TRUE and isPresent(edges, nedges, v2)):
            print("rejecting: "),
            print(edges[j][0]),
            print(edges[j][1]),
            print(edges[j][2])
        else:
            edges[j][2] = -edges[j][2]
            print("present: "),
            print(edges[j][0]),
            print(edges[j][1]),
            print(-edges[j][2])
            nspanedges = nspanedges + 1
            if(nspanedges == nvert -1):
                return 0
    print("No spanning tree exists for the graph")

def main():
    edges = [[0,1,16],[0,4,19],[0,5,21],[1,2,5],[1,3,6],[1,5,11],[2,3,10],[3,4,18],[3,5,14],[4,5,33]]
    nedges = len(edges)
    spanning(edges, nedges)

main()






