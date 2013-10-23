# Chapter 27.6
#  IMPLEMENTATION OF A B-TREE


class queue:
    def __init__(self):
        self.front = self.rear = qnode()

class qnode:

    def __init__(self):
        self.op = node()
        self.next = None

def qEmpty(q):
    if(q == None):
        return 1
    else:
        return 0

def qPush(q, op):
    # pushes op at q.rear
    ptr =  qnode()
    ptr.op = op
    if(qEmpty(q) == 1):
        q = queue()
        q.front = ptr
    else:
        q.rear.next = ptr
    q.rear = ptr
    return q

def qPop(q):
    # pops op from q->front
    #print("we are here")
    ptr =  q.front
    if(qEmpty(q) == 1):
       return  None,None
    if(qEmpty(q.front) == 1):
        return None,None
    q.front = q.front.next
    if(qEmpty(q) == 1):
        q.rear = None
    op = ptr.op
    return q, op

# /*************************** b.c ****************************/
K = 5
FALSE = 0
TRUE = 1

class node:
    def __init__(self):
        self.val = [0 for i in range(K)] # data in the node
        self.ptr = [None for i in range(K+1)] # pointers to other nodes in the node
        self.nptr = 0 # no of pointers in the node = non-null ptrs
        self.nval = 0 # no of values in the node

def bNew():
    # returns a new initialized node
    tree = node()
    tree.nval = tree.nptr = 0
    return tree

def insertVal(tree, val, ptr):
    # insert (val, ptr) in node pointed to by tree without any checks
    i = 0
    while(i < tree.nval  and tree.val[i] < val):
        i = i + 1
        """
        // the val should be inserted at tree->val[i].
   // shift-next the next values by one position.
"""
    for j in range(tree.nval-1, i-1, -1):
        tree.val[j+1] = tree.val[j]
        tree.ptr[j+2] = tree.ptr[j+1]
    # insert val now at i
    tree.val[i] = val
    tree.nval = tree.nval + 1
    tree.ptr[i + 1] = ptr
    if(ptr != None):
        tree.nptr = tree.nptr + 1
    print("val " + str(val) + " inserted at position "),
    print(str(i) + " , tree-> nptr= " +str(tree.nptr)),
    print("nval = " +str(tree.nval))
    return tree
def getSplitNode(tree):
    # returns a new node containing vals and pointers from tree
    ptr = bNew()
    j = 0
    for i in range((K -1)/2+1, K):
        ptr.val[j] = tree.val[i]
        j = j + 1
    ptr.nval = K/2
    tree.nval = K-K/2-1
    j = 0
    for i in range((K -1)/2+1, K+1):
        ptr.ptr[j] = tree.ptr[i]
        j = j + 1
    if(tree.nptr > 0):
        ptr.nptr = K/2+1
        tree.nptr =K-K/2
    else:
        tree.nptr = ptr.nptr = 0
    return ptr

def bMakeChanges(tree, ptr, parent):
    """
    /*
    * last val of tree contains an extra val which should be
    * inserted in parent.
    * if parent == NULL, then tree was root.
    * tree = parent->ptr[i] if parent is NOT NULL.
    */
"""
    # extract the last value from tree
    val = tree.val[tree.nval]
    print(val)
    print("in bMake Changes()")
    if(parent == None):
        parent = bNew()
        parent.ptr[0] = tree
        parent.nptr = 1
    if(parent.nval < K-1):
        parent = insertVal(parent, val, ptr)
    else:
        print("parent is full")
        parent = insertVal(parent, val, ptr)
        return getSplitNode(parent)
    return parent

def bInsert(tree, val):
    """
     /*
    * calls insert to insert val in tree.
    * if the return node is diff from tree, that means a new node has
    * been created. Thus calls bMakeChanges().
    */
"""
    ptr = insert(tree, val)
    if(ptr != tree):
        return bMakeChanges(tree, ptr, None)
    return tree

def insert(tree, val):
    """
    /*
    * inserts val in tree.
    * returns tree if there is no change.
    * if there is creation of a new node then the new node is returned.
    */
"""
    if(tree.nptr > 0):
        i = 0
        while(i < tree.nval and tree.val[i]<val ):
            i = i+ 1
        print("\tval should be inserted in tree->ptr[" +str(i)+"]")
        ptr = insert(tree.ptr[i], val)
        if(ptr != tree.ptr[i]):
            return bMakeChanges(tree.ptr[i], ptr, tree)
        return tree
    else:
        if(tree.nval < K-1):
            tree = insertVal(tree, val, None)
            return tree
        else:
            print("\tleaf is full.\n")
            tree = insertVal(tree, val, None)
            # now break the leaf node.
            return getSplitNode(tree)


def getAdjTree(tree, offset, parent, treeindex):
    newindex = treeindex + offset
    if(newindex >=0 and newindex < parent.nptr):
        return parent.ptr[newindex]
    return None


def combineNodes(left, right):
    # left += right.
    nptrleft = left.nptr
    for i in range(right.nval):
        left.val[left.nval] = right.val[i]
        left.nval = left.nval+1
    for i in range(right.nval):
        left.ptr[nptrleft+i] = right.ptr[i]
    if(left.nptr > 0):
        left.nptr += i
    return left, right

def getNextVal(ptr):
    if(ptr.nptr > 0):
        return getNextVal(ptr.ptr[0])
    return ptr.val[0]


"""
    /*
    * remove (val, ptr) at position i from tree without any checks.
    * and return tree->ptr[i+1].
    */
"""
def deleteVal(tree, i):
    rightptr = tree.ptr[i+1]
    for i in range(i+1, tree.nval):
        tree.val[i-1] = tree.val[i]
        tree.ptr[i] = tree.ptr[i+1]
    tree.nval = tree.nval - 1
    if(tree.nptr > 0):
        tree.nptr = tree.nptr - 1
    return tree

def bApplyChanges(tree, parent, treeindex):
    offset = -1
    if(parent != None and tree.nval == K/2):
        return tree
    elif(parent == None and tree.nval == 0):
        return tree.ptr[0]
    elif(parent == None):
        return tree
    # parent is full
    adjtreeleft = getAdjTree(tree, offset, parent, treeindex) #define the function
    adjtree = adjtreeleft
    if(adjtree == None or (adjtree != None and adjtree.nval <= K/2)):
        offset = 1
        adjtree = getAdjTree(tree, offset, parent, treeindex)
        if(adjtree == None or (adjtree != None and adjtree.nval <= K/2)):
            if(adjtree == None):
                adjtree = adjtreeleft
                offset = -1
            parentvalindex = (2*treeindex+offset)/2
            parentval = parent.val[parentvalindex]
            parent = deleteVal(parent, parentvalindex)
            if(offset == -1):
                adjtree.val[adjtree.nval] = parentval
                adjtree.nval = adjtree.nval + 1
                print("32")
                adjtree, tree= combineNodes(adjtree, tree)
                returntree = adjtree
            else:
                tree.val[tree.nval] = parentval
                tree.nval = tree.nval + 1
                tree, adjtree = combineNodes(tree, adjtree)
                returntree = tree
            return returntree
        else:
            adjtreevalindex = 0
            returntree = adjtree
    else:
        adjtreevalindex = adjtree.nval - 1
        returntree = tree
    parentvalindex=(2*treeindex+offset)/2
    tree = insertVal(tree, parent.val[parentvalindex], returntree.ptr[0])
    parent.val[parentvalindex] = adjtree.val[adjtreevalindex]
    returntree.ptr[0] = deleteVal(adjtree, adjtreevalindex)
    return tree

def delete(tree, val, i, parent, treeindex):
    if(tree.nptr == 0):
        tree = deleteVal(tree, i)
    else:
        nextval = getNextVal(tree.ptr[i+1])
        tree.val[i] = nextval
        tree.ptr[i+1] = bDelete(tree.ptr[i+1], nextval, tree, i + 1)
    return bApplyChanges(tree, parent, treeindex)

def bDelete(tree, val, parent, treeindex):
    i = 0
    while(i < tree.nval and tree.val[i] < val):
        i = i + 1
    if(tree.val[i] == val):
        print("val " +str(val) + " found at " + str(i))
        return delete(tree, val, i, parent, treeindex)
    elif(tree.nptr > 0):
        tree.ptr[i] = bDelete(tree.ptr[i], val, tree, i)
        return bApplyChanges(tree, parent, treeindex)
    else:
        print("val " +str(val) + " does not exist")
        return tree

def bPrintFormatted(tree):
    ptr = node()
    q = None
    q = qPush(q, tree)
    q =qPush(q,None)
    i = 0
    print("-----------------------------------------------")
    while(qEmpty(q) == 0):
        q, ptr = qPop(q)
        if(ptr != None):
            while(i < ptr.nval -1):
                print(str(ptr.val[i]) + "-"),
                i = i + 1
            if(i< ptr.nval):
                print(ptr.val[i]),
            for i in range(0,ptr.nptr):
                q = qPush(q,ptr.ptr[i])

        else:
            print("\n")
            if(qEmpty(q) == 0):
                q = qPush(q, None)
        i = 0
    print("--------------------------------------------------------")



def main():
    tree = bNew()
    tree = bInsert(tree, 1)
    tree = bInsert(tree, 2)
    tree = bInsert(tree, 4)
    tree = bInsert(tree, 3)
    tree = bInsert(tree, 5)
    tree = bInsert(tree, 6)
    tree = bInsert(tree, 7)
    tree = bInsert(tree, 8)
    tree = bInsert(tree, 9)
    bPrintFormatted(tree)
    tree = bDelete(tree, 6, None, -320)
    bPrintFormatted(tree)
    tree = bDelete(tree, 9, None, -320)
    bPrintFormatted(tree)




main()


