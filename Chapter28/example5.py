#Chapter 28.5
#FINDING THE SHORTEST PATH BY USING AN ADJACENCY MATRIX

MAXINT = 99999
MAXVERTICES =10
FALSE = 0
TRUE = 1

def Print(cost, nvert):
    #prints cost matrix
    for i in range(nvert):
        for j in range(nvert):
            print(cost[i][j]),
        print("\n")

def choose(dist, s, nvert):
    #/*
     #* returns vertex u such that:
     #* dist
    u = -1
    mindist = MAXINT
    for i in range(nvert):
        if(s[i] == FALSE and dist[i] <= mindist):
            u = i
            mindist = dist[i]
    return u

def sssp(v, cost, dist, nvert):
#/*
     #* finds shortest path from v to all other vertices.
     #* cost is the cost matrix.
     #* dist is the vector in which output will be written.
     #* nvert is no of vertices in the graph.
     #*/
    s = [0 for i in range(MAXVERTICES)]
    for i in range(nvert):
        s[i] = FALSE
        dist[i] = cost[v][i]
    s[v] = TRUE
    dist[v] = 0
    num = 1
    while(num < nvert -1):
        u = choose(dist, s, nvert)
        s[u] = TRUE
        num = num + 1
        for w in range(nvert):
            if(s[w] == FALSE and dist[u]+cost[u][w] < dist[w]):
                dist[w] = dist[u] + cost[u][w]
    return dist

def printDist(v, dist, nvert):
  #/*
     #* prints distance matrix which shows min distance of each vertex
     #* from v.
     #*/
    print("min dist from vertex " +str(v))
    for i in range(nvert):
        print("dist[" + str(i) +"] =" + str(dist[i]))

def main():
    cost = [[0,2,2,1],[3,0,4,1], [5,16,0,9], [1,1,2,0]]
    dist = [0 for i in range(MAXVERTICES)]
    nvert = 4
    dist = sssp(2,cost, dist, nvert)
    printDist(2, dist, nvert)

main()

