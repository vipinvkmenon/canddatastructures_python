# Chapter 26.2
#  MAXIMIZE A COMBINATION OF STRINGS -THE SECOND METHOD

MININT = -1000
MAXVERTICES = 10
MAXPATHVERT = 3
def printCosts(a, nvert, pathvert):
    # prints min cost matrix a
    for i in range(nvert):
        for j in range(nvert):
            if(a[i][j] <= MININT):
                print("M(" + str(pathvert[i][j]) +") "),
            else:
                print(str(a[i][j]) + "(" + str(pathvert[i][j]) + ")" ),
        print("\n")
    print("\n")

def getMaxSum(a, b, i, j, k, h1, h2):
    '''
     /*
    * find such h1 and h2 that b[h1][i][k]+b[h2][k][j] is max and > a[i][j];
    * and h1+h2 -1 < MAXPATHVERT;
    * return the sum.
    */
'''
    maxsum = 0
    h1 = h2 = -1
    for p in range(2, MAXPATHVERT):
        for q in range(p, MAXPATHVERT + 1):
            if(p+q -1 <= MAXPATHVERT and b[p][i][k]>0 and b[q][k][j]>0 and b[p][i][k]+b[q][k][j] > maxsum):
                maxsum = b[p][i][k]+b[q][k][j]
                h1=p
                h2=q
    if(maxsum > a[i][j]):
        return maxsum, h1, h2
    h1 = h2 = -1
    return -1, h1, h2

def allCosts(cost, a, nvert):
    h1 = h2 = 0
    pathvert = [[0 for i in range(MAXVERTICES)] for i in range(MAXVERTICES)]
    b = [[[0 for i in range(MAXVERTICES)] for i in range(MAXVERTICES)] for i in range(MAXPATHVERT+1)]
    for i in range(nvert):
        for j in range(nvert):
            a[i][j] = cost[i][j]
            pathvert[i][j] = 2
            b[2][i][j] = cost[i][j]
    printCosts(a, nvert, pathvert)
    for l in range(2, MAXPATHVERT + 1):
        for k in range(nvert):
            for i in range(nvert):
                for j in range(nvert):
                    Sum, h1, h2 = getMaxSum(a, b, i, j, k, h1, h2)
                    if(Sum != -1 and h1 != -1 and a[i][j] >= 0):
                        a[i][j] = Sum
                        b[h1 +h2 - 1][i][j] = Sum
                        pathvert[i][j] = h1 + h2 - 1
                printCosts(a, nvert, pathvert)


def main():
    cost = [[0,50,10,MININT,45,MININT], [MININT,0,15,MININT,10,MININT], [20,MININT,0,15,MININT,MININT], [MININT,20,MININT,0,35,MININT], [MININT,MININT,MININT,30,0,MININT], [MININT,MININT,MININT,3,MININT,0]]
    print(len(cost))
    a = [[0 for i in range(MAXVERTICES)] for i in range(MAXVERTICES)]
    nvert = 6
    allCosts(cost, a, nvert)

main()
