# Chapter 25.5
# MEMORY MANAGEMENT USING VARIOUS SCHEMES

N = 100
FALSE = 0
TRUE = 1
class node:

    def __init__(self):
        self.ptr = 0
        self.size = 0
        self.next = None

global mem
mem =  0 #[0 for i in range(N)]
global freelist
freelist = node()

def init():
    global mem
    global freelist
    # init freelist to contain the whole mem.
    ptr = node()
    ptr.ptr = mem
    ptr.size = N
    freelist.next = ptr

def removenode(ptr, prev):
    # remove a node ptr from the list whose previous node is prev.
    prev.next = ptr.next
    del ptr
    return prev

def firstfit(size):
    # returns ptr to free pool of size size from freelist.
    global freelist
    prev = freelist
    ptr = prev.next
    while(ptr != None):
        if(ptr.size > size):
            memptr = ptr.ptr
            ptr.size -= size
            ptr.ptr= ptr.ptr[size]
            return memptr
        elif(ptr.size == size):
            memptr = ptr.ptr
            ptr, prev = removenode(ptr, prev)
            return memptr
        prev = ptr
        ptr = ptr.next
    return None

def nextfit(size):
    # returns ptr to free pool of size size from freelist
    # the free pool is second allocatable block instead of first
    # if no second block then first is returned
    global freelist
    isSecond = FALSE
    prev = freelist
    while(ptr != None):
        if(ptr.size >= size and isSecond == FALSE):
            isSecond = TRUE
            firstprev = prev
            firstptr = ptr
        elif (ptr.size > size and isSecond == TRUE):
            memptr = ptr.ptr
            ptr.size -= size
            ptr.ptr = ptr.ptr[size]
            return memptr
        elif(ptr.ptr == size and isSecond == TRUE):
            memptr = ptr.ptr
            ptr, prev = removenode(ptr, prev)
            return memptr
        prev = ptr
        ptr = ptr.next
    # ptr is NULL
    ptr = firstptr
    prev = firstprev
    if(ptr.size > size and isSecond == TRUE):
        memptr = ptr.ptr
        ptr.size -= size
        ptr.ptr = ptr.ptr[size]
        return memptr
    elif(ptr.size == size and isSecond == TRUE):
        memptr = ptr.ptr
        ptr, prev = removenode(ptr, prev)
        return memptr
    else:
        return None

def bestfit(size):
    # returns ptr to free pool of size size from freelist.
    # the allocated block's original size - size is min in the freelist
    global freelist
    minwaste = N + 1
    minptr = None
    prev = freelist
    ptr = prev.next
    while(ptr != None):
        if(ptr.size >= size and ptr.size - size < minwaste ):
            minwaste = ptr.size - size
            minptr = ptr
            minprev = prev
        prev = ptr
        ptr = ptr.next
    if(minptr == None):
        return None
    ptr = minptr
    prev = minprev
    if(ptr.size > size):
        memptr = ptr.ptr
        ptr.size -= size
        ptr.ptr += size
        return memptr
    elif (ptr.size == size):
        memptr = ptr.ptr
        prev = removenode(ptr, prev)
        return memptr
    return None

def addtofreelist(memptr, size):
    # add memptr of size to freelist
    # remember that block ptrs are sorted on mem addr
    global freelist
    prev = freelist
    ptr = prev.next
    while(ptr!= None and id(ptr.ptr) < id(memptr)):
        prev = ptr
        ptr = ptr.next
    newptr = node()
    newptr.ptr = memptr
    newptr.size = size
    newptr.next = ptr
    prev.next = newptr

def coalesce():
    # combine adj blocks of list if necessary.
    global freelist
    prev = freelist
    ptr = prev.next
    while(ptr != None):
        # check for prev mem addr and size against ptr->ptr
        if(prev != freelist and id(prev.ptr) + prev.size == id(ptr.ptr)):
            # prev->size += ptr->size
            prev.next = ptr.next
            del(ptr)
            ptr = prev
        prev = ptr
        ptr = ptr.next

def memalloc(size):
    # return ptr to pool of mem of the size
    # return NULL if NOT available
    # ptr-sizeof(int) contains size of the pool allocated, like malloc
    ptr = bestfit(size + 4) # change this to firstfit() or nextfit().
    print("allocating " + str(size) + " using bestfit...\n")
    if(ptr == None):
        return None
    ptr = size
    return (ptr + 4)

def memfree(ptr):
    # adds ptr to freelist and combine adj blocks if necessary
    #  size of the mem being freed is at ptr-sizeof(int).
    size = ptr - 4
    print("freeing " +str(size) )
    addtofreelist(ptr - 4,size + 4)
    coalesce()

def printfreelist():
    global freelist
    ptr = freelist.next
    while(ptr):
        print(id(ptr.ptr)),
        print(ptr.size),
        ptr = ptr.next
    print("\n")

def main():
    init()
    printfreelist()
    p1 = memalloc(10)
    printfreelist()
    p2 = memalloc(15)
    printfreelist()
    p3 = memalloc(23)
    printfreelist()
    p4 = memalloc(3)
    printfreelist()
    p5 = memalloc(8)
    printfreelist()
    memfree(p1)
    printfreelist()
    memfree(p5)
    printfreelist()
    memfree(p3)
    printfreelist()
    p1 = memalloc(23)
    printfreelist()
    p1 = memalloc(23)
    printfreelist()
    memfree(p2)
    printfreelist()
    p1 = memalloc(3)
    printfreelist()
    memfree(p4)
    printfreelist()
    p2 = memalloc(1)
    printfreelist()
    memfree(p1)
    printfreelist()
    memfree(p2)
    printfreelist()






main()



