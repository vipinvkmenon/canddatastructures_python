#Chapter 23.3
# MULTIPLY TWO SPARSE MATRICES

M = 10
P = 7
N = 8

def ftrans(a, b):
    # finds fast-transpose of a in b.
    n = a[0][1]
    terms = a[0][2]
    b[0][0] = n
    b[0][1] = a[0][0]
    b[0][2] = terms
    if( terms <= 0 ):
        return 0
    for i in range(n):
        t[i] = 0
    for i in range(1, terms+1):
        t[a[i][1]] = t[a[i][1]] + 1
    temp = t[0]
    t[0] = 1
    for i in range(1, n):
        temp2 = t[i]
        t[i] = t[i-1]+temp
        temp = temp2
    for i in range(1, terms):
        j = t[a[i][1]]
        b[j][0] = a[i][1]
        b[j][1] = a[i][0]
        b[j][2] = a[i][2]
    return a, b

def printMatrix(a):
    #prints matrix in the form of a 3-tuple

    nterms = a[0][2]
    print("rows : " + str(a[0][0]) + " cols: " + str(a[0][1]) + " vals : " +str(a[0][2]))
    for i in range(1,nterms+1):
        print("a[" + str(a[i][0]) + "][" + str(a[i][1]) + "] = " + str(a[i][2]))
    print("\n")

def insert(c, row, col, val):
    # insert or add the triplet (row,col,val) in c.
    # update c[0][2] if necessary.
    terms = c[0][2]
    i = 1
    while(i <= terms and c[i][0] < row):
        i = i + 1
    while(i <= terms and c[i][1] < col):
        i = i + 1
    if(i <= terms and c[i][1] == col):  # already inserted.
        c[i][2] += val
    else:  # a new entry should be inserted at i
        c[i][0] = row
        c[i][1] = col
        c[i][2] = val
        c[0][2] = c[0][2] + 1
    return c

def mmult(a, b, c):
    # c = a*b
    mn = M*N
    aterms = a[0][2]
    bterms = b[0][2]
    rowsofb = b[0][0]
    c[0][0] = a[0][0]
    c[0][1] = b[0][1]
    for i in range(mn+1):
        c[i][2] = 0
    # fill t[] : t[i] points to row of b where actual row i starts
    # last+1 entry is also maintained for easing loops
    t = [0 for i in range(rowsofb+1)]
    for i in range(1,bterms+1):
        t[b[i][0]] = t[b[i][0]] + 1
    temp = t[0]
    t[0] = 1
    for i in range(1,rowsofb+1):
         temp2 = t[i]
         t[i] = t[i-1]+temp
         temp = temp2
    # now start mult
    for i in range(1,aterms+1):
         arow = a[i][0]
         acol = a[i][1]
         aval = a[i][2]
         brow = acol
         browstart = t[brow]
         browend = t[brow+1]
         for j in range(browstart,browend):
             c = insert( c, arow, b[j][1], aval*b[j][2] )
    return c

def main():
    a = [[4,2,3], [0,1,2], [1,0,3], [3,1,4]]
    b = [[2,3,3], [0,2,5], [1,0,7], [1,1,6]]
    c = [[0 for i in range(3)] for i in range(M*N+1)]
    printMatrix(a)
    printMatrix(b)
    c = mmult( a, b, c )
    printMatrix(c)

main()


















