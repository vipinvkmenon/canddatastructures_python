# Chapter 27.1
# WRITE A NON-RECURSIVE VERSION OF PREORDER

# /**************** stack.c **********************/

SUCCESS = 0
ERROR = -1

class snode:
    def __init__(self):
        self.data = None
        self.next = None


def sPush(s, data):
    # push data at stop.
    ptr = snode()
    ptr.data = data
    ptr.next = s
    s = ptr
    return SUCCESS,s

def sPop(s):
    # returns data at stop
    if(sEmpty(s) == 1):
        print("ERROR : popping from empty stack.")
        return None
    data = s.data
    ptr = s
    s =s.next
    return data, s

def sEmpty(s):
    if(s == None):
        return 1
    else:
        return 0

# /**************** main.c **********************/

class tnode:

    def __init__(self):
        self.data = 0
        self.right = None
        self.left = None
global tree
tree = None
s1 = None
s2 = None

def tInsert(data):
    # insert data into global tree.
    global tree
    ptr = tnode()
    ptr.data = data
    d,tree, ptr = tInsertptr(tree, ptr)

def tInsertptr(tree, ptr):
    # inserts ptr into tree recursively.
    if(tree != None):
        if(ptr.data < tree.data):
            d,tree.left,ptr = tInsertptr(tree.left, ptr)
        else:
            d,tree.right, ptr = tInsertptr(tree.right, ptr)
    else:
        tree = ptr
    return SUCCESS,tree, ptr

def tPrint(tree):
    #prints tree in inorder recursively
    if(tree != None):
        print("\ngoing left of " + str(tree.data))
        tPrint(tree.left)
        print(tree.data),
        print("\ngoing right of " + str(tree.data))
        tPrint(tree.right)
        print(tree.data),

def tIterPostorder(tree):
    # prints tree in postorder iteratively using 2 stacks.
    s1 = None
    s2 = None
    if( tree != None):
        d, s1 = sPush(s1, tree)
        while(sEmpty(s1) == 0):
            t, s1 = sPop(s1)
            d, s2 = sPush(s2, t)
            if(t.left != None):
                d, s1 = sPush(s1, t.left)
            if(t.right != None):
                d, s1 = sPush(s1, t.right)
        while(sEmpty(s2) == 0):
            d,s2 = sPop(s2)
            print(d.data),
        print("\n")

def main():
    tInsert(4)
    tInsert(2)
    tInsert(5)
    tInsert(1)
    tInsert(3)
    tInsert(6)
    #//tInsert(7)
    tPrint(tree)
    print("\n")
    tIterPostorder(tree)


main()


