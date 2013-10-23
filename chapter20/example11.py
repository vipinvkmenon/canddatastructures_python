# Chapter 20.11
# REPRESENTATION OF SPARSE MATRICES

class snode:  # Node class

    def __init__(self):
        self.row = 0
        self.col = 0
        self.val = 0
        self.link = None


def insert(p, r, c, val):  # Insert function
    if(p == None):
        p = snode()
        if(p == None):
            print("Error")
            exit()
        p.row = r
        p.col = c
        p.val = val
    else:
        p.link = insert(p.link, r, c, val)
    return(p)

def sadd(p,q):  # Add the matrices
    r = None
    while((p != None) and (q != None)):
        if(p.row < q.row):
            r = insert(r,p.row, p.col, p.val)
            p = p.link
        else:
            if(p.row < q.row):
                r = insert(r, q.row, q.col, q.val)
                q = q.link
            else:
                if(p.col > q.col):
                    r = insert(r, q.row, q.col, q.val)
                else:
                    val = p.val + q.val  # Add coefficients
                    r = insert(r, p.row, p.col, val)
                    p = p.link
                    q = q.link
    if(p != None):
        r = insert(r, p.row, p.col, p.val)
        p = p.link
    while(q != None):
        r = insert(r, q.row, q.col,q.val)
        q = q.link
    return(r)




def printlist(p):  #printlist
    print("The resultatn is\n")
    while(p !=None):
        print(str(p.row) + " " + str(p.col) + " " + str(p.val))
        p = p.link


def main():  # Main Function
    s1= None
    s2 = None
    result = None
    print("Enter the number of non-zero terms in the sparse matrix1")
    n = int(raw_input())
    print("Enter the terms in the sparse matrix1 in the increasing")
    print("order of row indices and for the same row index in the increasing order of")
    print("row indices and for the same row index in the increasing order of column")
    print("indices \n")
    while(n > 0):
        print("Enter trow col and value")
        r = int(raw_input())
        c = int(raw_input())
        val = int(raw_input())
        s1 = insert(s1, r, c, val)
        n = n -1
    print("Enter the number of non-zero terms in the sparse matrix2")
    n = int(raw_input())
    print("Enter the terms in the sparse matrix2 in the increasing")
    print("order of row indices and for the same row index in the increasing order of")
    print("row indices and for the same row index in the increasing order of column")
    print("indices \n")
    while(n > 0):
        print("Enter row col and value")
        r = int(raw_input())
        c = int(raw_input())
        val = int(raw_input())
        s2 = insert(s2, r, c, val)
        n = n -1
    result = sadd(s1,s2)
    print("The result is")
    printlist(result)

main()  # Main function entry