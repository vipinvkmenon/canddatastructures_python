# Chapter 25.7
# GARBAGE COLLECTION- THE SECOND METHOD


TRUE = 1
FALSE = 0

class snode:
    def __init__(self):
        self.op = 0
        self.next = None

def sEmpty(s):
    if(s == None):
        return TRUE
    else:
        return FALSE

def sPush(s, op):
    #pushes op in stack s.
    ptr = snode()
    ptr.op = op
    ptr.next = s
    s = ptr
    return s

def sTop(s):
    # returns top op from stack s without popping
    if(sEmpty(s) == None):
        return None
    return s.op

def sPop(s):
    # pops op from top of stack s.
    ptr = s
    if(sEmpty(s) == TRUE):
        return None
    s = s.next
    op = ptr.op
    return op

class node:

    def __init__(self):
        self.mark = 0
        self.val = 0
        self.tag = 0
        self.horiz =None
        self.vert = None

def newNode():
    return node()

def createList():
    # return a dummy list created
    ptr = None
    s = None
    nineptr = node()
    ptr =newNode()
    s = sPush(s, ptr)
    ptr.val = 1
    ptr.horiz = node()
    ptr = ptr.horiz
    s = sPush(s, ptr)
    ptr.val = 2
    ptr.vert = node()
    s = sPush(s, ptr)
    ptr.val = 3
    ptr.vert = node()
    ptr = ptr.vert
    ptr.val = 4
    ptr = sPop(s)
    ptr.horiz = newNode()
    ptr = ptr.horiz
    ptr.val = 5
    ptr.horiz = newNode()
    ptr = ptr.horiz
    s = sPush(s, ptr)
    sixptr = ptr
    ptr.val = 6
    ptr.vert = newNode()
    ptr =ptr.vert
    ptr.val = 7
    ptr= sPop(s)
    ptr.horiz = newNode()
    ptr = ptr.horiz
    ptr.val = 8
    ptr = sPop(s)
    ptr.horiz = newNode()
    s = sPush(s, ptr)
    nineptr = ptr
    ptr.val = 9
    ptr.vert = newNode()
    ptr = ptr.vert
    ptr.val = 10
    ptr.horiz = newNode()
    ptr = ptr.horiz
    ptr.val = 11
    ptr = sPop(s)
    ptr.horiz = newNode()
    ptr = ptr.horiz
    ptr.vert = nineptr  # an internal link
    ptr.val = 12
    ptr.horiz = newNode()
    ptr = ptr.horiz
    s = sPush(s, ptr);
    ptr.val = 13
    ptr.vert = newNode()
    ptr = ptr.vert
    ptr.val = 14
    ptr.horiz = sixptr  # an internal link
    ptr = sPop(s)
    return sPop(s)

def markList(ptr):
    # print the horiz and vert lists iteratively without using a stack
    p = ptr
    t = None
    #-----------------
    print("p.val = " + str(p.val))
    q = p.vert
    if(q):
        if(q.mark == FALSE and q.tag == FALSE):
            q.tag = TRUE
            p.tag = TRUE
            p.vert = t
            t = p
            p = q
        else:
            q.mark = TRUE
            p, q, t = label(p, q, t)
    else:
        p, q, t = label(p, q, t)
    while(t):
        print("p.val = " + str(p.val))
        q = p.vert
        if(q):
            if(q.mark == FALSE and q.tag == FALSE):
                q.tag = TRUE
                p.tag = TRUE
                p.vert = t
                t = p
                p = q
            else:
                q.mark = TRUE
                p, q, t = label(p, q, t)  # label
        else:
            p, q, t = label(p, q, t)  # goto label


def label(p,q,t):
    q = p.horiz
    if(q):
        if(q.mark == FALSE and q.tag == FALSE):
            q.mark = TRUE
            p.horiz = t
            t= p
            p = q
        else:
            q.mark = TRUE
            p, q, t = label2(p, q, t)  # goto label2
    else:
        p, q, t = label2(p,q, t)  # goto labele2
    return p, q, t


def label2(p, q, t):
    while(t):
        q = t
        if(q.tag):
            t = q.vert
            q.vert = p
            q.tag = FALSE
            p = q
            p,q,t = label(p, q, t)
    return p, q, t


def main():
    head = createList()
    markList(head)

main()
