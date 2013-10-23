# Chapter 27.1
# WRITE A NON-RECURSIVE VERSION OF PREORDER

# /**************** stack.c **********************/

SUCCESS = 0
ERROR = -1

class snode:
    def __init__(self):
        self.data = None
        self.next = None

stop = None # signifies empty stack.

def sPush(data):
    global stop
    # push data at stop.
    ptr = snode()
    ptr.data = data
    ptr.next = stop
    stop = ptr
    return SUCCESS

def sPop():
    # returns data at stop
    global stop
    if(sEmpty == 1):
        print("ERROR : popping from empty stack.")
        return None
    data = stop.data
    ptr = stop
    stop =stop.next
    return data

def sEmpty():
    global stop
    if(stop == None):
        return 1
    else:
        return 0

# /**************** queue.c **********************/

class qnode:

    def __init__(self):
        self.data = None
        self.next = None

front = None #signifies empty queue.
rear = None

def qInsert(data):
    global front
    global rear
    # inserts data at rear
    ptr = qnode()
    ptr.data = data
    ptr.next = None
    if(qEmpty == 1):
        front = ptr
    else:
        rear.next = ptr
    rear = ptr
    return SUCCESS

def qRetrieve():
    global front
    global rear
    if(qEmpty() == 1):
        print("ERROR : retrieving from empty queue.")
        return None
    data = front.data
    if(qEmpty() == 1):
        rear = None
    return data

def qEmpty():
    global front
    if(front == None):
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

def tIterBFS(tree):
    # prints tree in breadth-first manner iteratively using a queue
    global front
    global rear
    if(tree != None):
        qInsert(tree)
        while(qEmpty() == 0):
            tree = qRetrieve()
            print("[[" + str(tree.data) + "]]"),
            if(tree.left != None):
                qInsert(tree.left)
            if(tree.right != None):
                qInsert(tree.right)

def tIterPreorder(tree):
    # prints tree in preorder iteratively using a stack.
    global stop
    if(tree != None):
        sPush(tree)
        while(sEmpty() == 0):
            tree = sPop()
            print("[[" + str(tree.data) + "]]"),
            if(tree.left != None):
                sPush(tree.left)
            if(tree.right != None):
                sPush(tree.right)


def main():
    global tree
    tInsert(4)
    tInsert(2)
    tInsert(6)
    tInsert(1)
    tInsert(3)
    tInsert(5)
    tInsert(7)
    print("tPrint()")
    tPrint(tree)
    print("\nIter preorder")
    tIterPreorder(tree)

main()
