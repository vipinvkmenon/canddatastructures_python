#Chapter 29.5
#  N-QUEENS PROBLEM


N = 10
FALSE = 0
TRUE = 1
def printMatrix(a, n):
    for i in range(n):
        for j in range(n):
            print(a[i][j]),
        print("")
    print("\n")

def getMarkedCol(a,n,row):
    #/*
     #* returns the column marked in row
     #*/
    for j in range(n):
        if(a[row][j] == TRUE):
            return j
    print("ERR0R:  No col marked in the row " + str(row))
    return -1

def feasable(a, n, row, col):
    #/*
     #* checks whether next queen can be kept at a[row][col].
     #*/
    for i in range(row):
        markedcol = getMarkedCol(a, n, i)
        if (markedcol == col or abs(row-i) == abs(col-markedcol)):
            return FALSE
    return TRUE

def NQueens(a, n , row):
        #/*
     #* solve n-queens problem. the solution is obtained using matrix a.
     #* the procedure is recursive. current row being considered is row.
     #* that means all the rows from 0 to row-1 are considered.
     #*/
    if(row<n):
        for j in range(n):
            if(feasable(a,n,row,j) == 1):
                a[row][j]= TRUE
                NQueens(a,n,row+1)
                a[row][j]=FALSE
            else:
                printMatrix(a, n)
    return a

def main():
    a =[[0 for i in range(N)]for i in range(N)]
    for i in range(8):
        for j in range(8):
            a[i][j] = 0
    a = NQueens(a,8,0)

main()






