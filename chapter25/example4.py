# Chapter 25.4
# MEMORY MANAGEMENT USING LISTS

N = 90
K = 10
SUCCESS = 0
ERROR = -1
global freelist
freelist  = None
global nodeptr
nodeptr= None

class node:

    def __init__(self):
        self.ptr = None
        self.next = None

class head:

    def __init__(self):
        self.next = node()
        self.bytes = 0

def init():
    # initialize the memory space.
    global freelist
    global nodeptr
    freelist = head()
    nodeptr = node()
    freelist.bytes = [0 for i in range(N)]
    for i in range(N/(K - 1), 0, -1):
        memfree(freelist.bytes[i])


def memalloc():
    #  returns a void
    # pointer to area from freelist
    global freelist
    global nodeptr
    if(freelist.next == None):
        return None
    nodeptr = freelist.next
    ptr =nodeptr.ptr
    freelist.next = freelist.next.next
    return(ptr)

def memfree(ptr):
    # adds ptr to freelist.
    if(ptr == None):
        return 0
    nodeptr = node()
    nodeptr.ptr = ptr
    nodeptr.next = freelist.next
    freelist.next = nodeptr

def Print():
    global freelist
    ptr = freelist.next
    while(ptr != None):
        print(id(ptr.ptr)),
        ptr = ptr.next
    print("\n")


def main():
    init()
    print("after init...\n")
    Print()
    p1 = memalloc()
    print("after memalloc(p1)...\n")
    p2 = memalloc()
    p3 = memalloc()
    Print()
    memfree(p1)
    memfree(p2)
    memfree(p3)
    print("after memfree(p1)...\n")
    Print()

main()



