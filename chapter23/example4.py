#Chapter 23.4
# MULTIPLY TWO SPARSE MATRICES_2

M = 10
P = 10
N = 10
DEFAULTVAL = 0
SUCCESS = 0
ERROR = -1

class node:
    def __init__(self):
        self.data = 0
        self.row = 0
        self.col = 0
        self.hnext = None
        self.vnext = None

class spmat:
    def __init__(self):
        self.rows = None
        self.cols = None

def sInit(mat, rows, cols):
    # initializt the matrix
    mat.rows = [node() for i in range(rows)]
    mat.cols = [node() for i in range(cols)]
    for i in range(rows):
        mat.rows[i].hnext = mat.rows[i]
        mat.rows[i].row = i
    for i in range(cols):
        mat.cols[i].vnext = mat.cols[i]
        mat.cols[i].col = i
    return mat

def sAdd(mat, row, col, data):
    # adds a new node to the sparse matrix.
    if(data == DEFAULTVAL):
        return 0, mat
    ptr = node()
    ptr.data = data
    ptr.row = row
    ptr.col = col
    g, mat.rows[row] = cRowInsert(mat.rows[row], ptr)
    g, mat.cols[col] = cColInsert(mat.cols[col], ptr)
    return SUCCESS, mat

def cRowInsert(head, dataptr):
    # inserts dataptr in appropriate row of sparse matrix.
    prev = head
    ptr = prev.hnext
    while(ptr != head and ptr.col < dataptr.col):
        prev = ptr
        ptr = ptr.hnext
    if(ptr != head and ptr.col == dataptr.col):
        # data already exists
        ptr.data += dataptr.data
        return SUCCESS, head
    # dataptr should be added between prev and ptr.
    dataptr.hnext = ptr
    prev.hnext = dataptr
    return SUCCESS, head

def cColInsert(head,dataptr):
    # inserts dataptr in appropriate col of sparse matrix.
    # Assume that cRowInsert() was called before.
    prev = head
    ptr = prev.vnext
    while(ptr != head and ptr.row < dataptr.row):
        prev = ptr
        ptr = ptr.vnext
    if(ptr != head and ptr.row == dataptr.row):  # data already exists
        return SUCCESS, head
    # dataptr should be added between prev and ptr
    dataptr.vnext = ptr
    prev.vnext = dataptr
    return SUCCESS, head

def cRowPrint(head):
    # print row
    print(head.row),
    ptr = head.hnext
    while(ptr != head):
        print(str(ptr.data) + "(" +str(ptr.row)+","+str(ptr.col)+")"),
        ptr = ptr.hnext
    print("\n")

def cColPrint(head):
    # print row
    print(head.col),
    ptr = head.vnext
    while(ptr != head):
        print(str(ptr.data) + "(" +str(ptr.row)+","+str(ptr.col)+")"),
        ptr = ptr.vnext
    print("\n")

def sHPrint(mat, rows):
    # print sparse matrix by traversing it row-wise.
    for i in range(rows):
        cRowPrint( mat.rows[i])
    print("\n")

def sVPrint(mat, cols):
    # print sparse matrix by traversing it col-wise.
    for i in range(cols):
        cColPrint( mat.cols[i])
    print("\n")

def sGetVal(a, row, col):
    # return a[row][col]
    head = a.rows + row
    ptr = head.hnext
    while(ptr != head):
        if(ptr.col == col):
            return ptr.data
    return DEFAULTVAL  # entry absent in matrix : default value 0.

def sMatMulBad(a, b, c):
    # original inefficient implementation of matrix mult.
    for i in range(M):
        for j in range(N):
            data = 0
            for k in range(P):
                data = sGetVal(a,i,k)*sGetVal(b,k,j)
                g, c = sAdd(c, i, j, data)
    return SUCCESS, c

def sMatMul(a, b, c):
    #  matrix multiplication
    for i in range(M):
        ptri = a.rows[i].hnext
        while(ptri != a.rows[i]):
            row = ptri.col
            ptrj=b.rows[row].hnext
            while(ptrj!=b.rows[row]):
                g,c = sAdd( c, i, ptrj.col, ptri.data*ptrj.data )
                ptrj = ptrj.hnext
            ptri = ptri.hnext
    return SUCCESS, c

def main():
    a = spmat()
    b = spmat()
    c = spmat()
    a = sInit(a,M,P)
    b = sInit(b,P,N)
    c = sInit(c,M,N)
    g, a = sAdd( a, 0,1, 2 )
    g, a = sAdd( a, 1,0, 3 )
    g, a = sAdd( a, 3,1, 4 )
    g, b = sAdd(b, 0,2, 5)
    g, b = sAdd(b, 1,0, 7)
    g, b = sAdd(b, 1,1, 6)
    sHPrint(a,M)
    sVPrint(b,P)
    g, c = sMatMul(a, b, c)
    sHPrint(c,M)
    sVPrint(c,N)

main()



