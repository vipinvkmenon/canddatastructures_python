#Chapter 28.7
#  THE M SHORTEST PATH

M = 8
MAXVERTICES = 10
MAXINT= 99999
FALSE = 0
TRUE = 1

def Print(cost, nvert):
    # prints the cost matrix
    for i in range(nvert):
        for j in range(nvert):
            print(cost[i][j]),
        print("\n")

def printCosts(a, nvert):
    for i in range(nvert):
        for j in range(nvert):
            print("cost[" + str(i) + "," +str(j) +"] = " + str(a[i][j]))

def allcosts(cost, a, nvert):
    # finds all pairs shortest paths and store in a[][].
    for i in range(nvert):
        for j in range(nvert):
            a[i][j] = cost[i][j]
    for k in range(nvert):
        for i in range(nvert):
            for j in range(nvert):
                if( a[i][k]+a[k][j] < a[i][j] ):
                    a[i][j] = a[i][k] + a[k][j]
    return cost, a

def main():
    cost = [[0,50,10,MAXINT,45,MAXINT], [MAXINT,0,15,MAXINT,10,MAXINT], [20,MAXINT,0,15,MAXINT,MAXINT],[MAXINT,20,MAXINT,0,35,MAXINT],[MAXINT,MAXINT,MAXINT,30,0,MAXINT],[MAXINT,MAXINT,MAXINT,3,MAXINT,0]]
    a = [[0 for i in range(MAXVERTICES)] for i in range(MAXVERTICES)]
    nvert = 6
    cost, a = allcosts(cost, a, nvert)
    printCosts(a, nvert)

main()

