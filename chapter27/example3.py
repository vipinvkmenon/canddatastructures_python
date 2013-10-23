# Chapter 27.3
# PREORDER TRAVERSAL OF A THREADED BINARY TREE


SUCCESS = 0
ERROR = -1
FALSE = 0
TRUE = 1

class node:

    def __init__(self):
        self.lchild = None
        self.rchild = None
        self.data = 0
        self.lthread = FALSE
        self.rthread = FALSE

# NOTE: since this is a threaded binary tree, there wont be any condition
# of type (ptr == NULL)

global tree
tree = node()

def tInit():
    global tree
    tree.lchild = tree.rchild = tree
    tree.lthread = TRUE
    tree.data = 99999999

def insucc(t):
    # find inorder successor of t
    temp = t.rchild
    if(t.rthread == FALSE):
        while(temp.lthread == FALSE):
            temp = temp.lchild
    return temp

def inpred(t):
    # find inorder predecessor of t
    temp = t.lchild
    if(t.lthread == FALSE):
        temp = temp.rchild
    return temp

def tInsertRight(s,t):
    t.rchild = s.rchild
    t.rthread = s.rthread
    t.lchild = s
    t.lthread = TRUE
    s.rchild = t
    s.rthread = FALSE
    if (t.rthread == FALSE):
        temp = insucc(t)
        temp.lchild = t
    return SUCCESS, s


def tInsertLeft(s,t):
    # insert t as left child of s
    t.lchild = s.lchild
    t.lthread = s.lthread
    t.rchild = s
    t.rthread = TRUE
    s.lchild = t
    s.lthread = FALSE
    if (t.lthread == FALSE):
        temp = inpred(t)
        temp.rchild = t
    return SUCCESS, s

def tGetNewNode(data):
    # returns a new node containing the data
    ptr = node()
    ptr.data = data
    ptr.lchild = ptr.rchild = None
    ptr.lthread = ptr.rthread = FALSE
    return ptr

def tInsert(t, data):
    # insert data in t recursively
    if(data < t.data):
        if(t.lthread == TRUE):
            d, t = tInsertLeft( t, tGetNewNode(data) )
        else:
            d,t = tInsert(t.lchild, data)
    else:
        if(t.rthread == TRUE):
            d, t = tInsertRight( t, tGetNewNode(data) )
        else:
            d,t = tInsert(t.rchild, data)
    return SUCCESS, t

def tPrint(t):
    # prints t inorder recursively without using threads
    if(t != tree):
        if(t.lthread == FALSE):
            tPrint(t.lchild)
        print(t.data)
        if(t.rthread == FALSE):
            tPrint(t.rchild)


def tPrintPreorder(t):
    #  prints tree preorder (no use of threads).
    global tree
    if(t != tree):
        print(t.data)
        if(t.lthread == FALSE):
            tPrintPreorder(t.lchild)
        if(t.rthread == FALSE):
            tPrintPreorder(t.rchild)

def tPrintInorder(t):
    global tree
    temp = tree
    temp = insucc(temp)
    if(temp != tree):
        print(temp.data)
    while(temp != tree):
        temp = insucc(temp)
        if(temp != tree):
            print(temp.data)

def main():
    global tree
    tInit()
    print(tree.data)
    tInsert(tree, 4)
    tInsert(tree, 2)
    tInsert(tree, 1)
    tInsert(tree, 3)
    tInsert(tree, 6)
    tInsert(tree, 5)
    tInsert(tree, 7)
    tPrint(tree.lchild)
    print("\n")
    tPrintPreorder(tree.lchild)

main()



