# Chapter 27.5
# HUFFMAN CODING

#/********************** huffman.q.h ************************/

class queue:

    def __init__(self):
        self.front = None
        self.rear =  None

class qnode:

    def __init__(self):
        self.op = 0
        self.next = None

def qPushBack(q, op):
    # pushes op at q.rear.
    ptr = qnode()
    ptr.op = op
    if(qEmpty(q) == 1):
        q = qnode()
        q.front = ptr
    else:
        q.rear.next = ptr
    q.rear = ptr
    return q

def qInsertSorted(q, op):
    # inserts val in sorted q and keeps new q sorted.
    ptr = qnode()
    ptr.op = op
    prev = None
    curr = q.front
    while(curr != None and curr.op.w < op.w ):
        prev = curr
        curr = curr.next
    if(curr == None and prev == None):  # q empty
        ptr.next = None
        q.rear = q.front = ptr
    elif(curr == None):
        ptr.next = None
        prev.next = q.rear = ptr
    elif(prev == None):
        ptr.next = curr
        q.front = ptr
    else:
        ptr.next = curr
        prev.next = ptr
    return q

def qPopFront(q):
    # pops op from q->front
    ptr = q.front
    if(qEmpty(q) == 1):
        return None
    q.front = q.front.next
    if(qEmpty(q) == 1):
        q.rear = None
    op = ptr.op
    return q, op

def qEmpty(q):
    if(q == None):
        return 1
    else:
        return 0


# /********************* huffman.c *************************/
MAXLEN = 80
FALSE = 0
TRUE = 1

class node:

    def __init__(self):
        self.w = ""
        self.val = 0
        self.left = self.right = None

def compare(e1, e2):
    """
    \/*
     * compare the two elements in e1 and e2.
     * each element is a vector of two elements.
     */"""
    if(e1[1] > e2[1]):
        return 1
    else:
        return 0

def printTree(t, outputstr):
    """
    /*
     * print the huffman codes for each element of t.
     * outputstr contains huffman code for t (NOT parent of t).
     * assumes t!=NULL.
     */
"""

    Str = "1"
    if(t.right != None):
        for i in range(len(Str)):
            outputstr[i] = Str[i]
        printTree(t.right, outputstr)
        outputstr[len(outputstr) - 1] = ""
    if(t.left != None):
        Str= "0"
        for i in range(len(Str)):
            outputstr[i] = Str[i]
        printTree(t.left, outputstr)
        outputstr[len(outputstr) - 1] = ""
    elif(t.right == None):
        print(t.val),
        print(t.w),
        print("".join(outputstr))

def buildTree(a, n):
    """
    /*
     * build a huffman tree using frequency in a[i][1] where a[0][j] indicates
     * the character
     * for that sort a on frequency.
     * n is the size of a.
     */"""
    t = None
    sortedq = None
    # sort a on frequency
    # qsort(a, n, len(a[0]), compare)
    # insert each element in tree.
    for i in range(n):
        temp = node()
        temp.w = a[i][0]
        sortedq = qPushBack(sortedq, temp)
    # assume n>0
    g = 1
    while(g == 1):
        t2 = node()
        sortedq, t1 = qPopFront(sortedq)
        if(qEmpty(sortedq) == 1):
            sortedq, t2 = qPopFront(sortedq)
        else:
            t = t1
            break
    t = node()
    t.w = t1.w + t2.w
    t.left = t1
    t.right = t2
    ptr = sortedq.front
    while(ptr != None):
        print(ptr.op.w),
        ptr = ptr.next
    print("\n")
    print("insertsorted"),
    print(t.w)
    sortedq = qInsertSorted(sortedq, t)
    return t

def main():
    a = [["a", 20], ["b", 23], ["c", 14], ["d", 56], ["e", 35], ["f", 29], ["g", 5]]
    outputstr = ["" for i in range(MAXLEN)]
    t = buildTree(a, len(a))
    if(t != None):
        printTree(t, outputstr)


main()

