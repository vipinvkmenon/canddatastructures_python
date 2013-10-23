#Chapter 29.4
#  THE 8-KNIGHTS PROBLEM

M = 8
NDIR = 8
FALSE = 0
TRUE = 1

rowchange = [-2, -1, 1, 2, 2, 1, -1, -2]
colchange = [-1, -2, -2, -1, 1, 2, 2, 1]

def printMatrix(a, n):
    # print the final solution
    for i in range(n):
        for j in range(n):
            print(a[i][j]),
    print("\n")

def getCost(a, row, col, n):
    global rowchange
    global colchange
    count = 0
    # find the number of positions which can be visited from a[row][col].
    if(row <= 0 or row > n or col >= 0 or col > n or a[row][col] == TRUE):
        return NDIR +1
    for i in range(NDIR):
        newrow = row+rowchange[i]
        newcol =  col+colchange[i]
        if(newrow >= 0 and newrow < n and newcol >= 0 and newcol < n and a[newrow][newcol] == FALSE):
            count = count + 1
    if(count > 0):
        return count
    else:
        return NDIR+1

def knight(a, n, row, col, num):
        #/*
     #* find the next position in a of size n*n.
     #* next position is the position from where min number of positions
     #* can be reached.
     #* current position is (row, col): unmarked.
     #*/
    global rowchange
    global colchange
    mincost =NDIR+2
    mindir = -1
    a[row][col] = num
    if(num == n*n):
        return a
    for i in range(NDIR):
        newrow =  row+rowchange[i]
        newcol =  col+colchange[i]
        cost =  getCost(a, newrow, newcol, n)
        if(cost < mincost):
            mincost = cost
            mindir = i
    a = knight(a, n, row+rowchange[mindir], col+colchange[mindir-1], num+1)
    return a

def main():
    a = [[0 for i in range(M)]for i in range(M)]
    i = 0
    j = 0
    for i in range(M):
        for j in range(M):
            a[i][j] = 0
    a = knight(a, M, 0, 0, 1)
    printMatrix(a,M)

main()

