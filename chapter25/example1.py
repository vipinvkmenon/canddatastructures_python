# Chapter 25.1
# IMPLEMENTATION OF POLYNOMIALS USING LINKED LISTS

class node:

    def __init__(self):
        self.coeff = 0
        self.power = 0
        self.next = None

def createPoly(n,v1):
    v1 = v1.split()
    p = None
    for i in range(0, len(v1)-1, +2):
        ptr = node()
        ptr.coeff = int(v1[i])
        i = i + 1
        ptr.power = int(v1[i])
        ptr.next = p
        p = ptr
    return p

def pPrint(p):
    ptr = p
    while(ptr != None):
        print(str(ptr.coeff) + "x" +str(ptr.power) + "+"),
        ptr = ptr.next
    print("\n")

def pSub(p1, p2):
    # return p1 - p2 recursievly
    ptr = node()
    if(p1 != None and p2 != None and p1.power == p2.power):
        ptr.coeff = p1.coeff - p2.coeff
        ptr.power = p1.power
        ptr.next = pSub(p1.next, p2.next)
    elif(p1 and ((p2 != None and p1.power < p2.power) or p2 == None)):
        ptr.coeff = p1.coeff
        ptr.power = p1.power
        ptr.next = pSub(p1.next,p2)
    elif(p2 and ((p1 != None and p1.power > p2.power) or p1 == None)):
        ptr.coeff = -p2.coeff
        ptr.power = p2.power
        ptr.next = pSub(p1,p2.next)

    else:
        return None
    return ptr

def pAdd(p1, p2):
    # return p1 - p2 recursievly
    ptr = node()
    if(p1 != None and p2 != None and p1.power == p2.power):
        ptr.coeff = p1.coeff + p2.coeff
        ptr.power = p1.power
        ptr.next = pAdd(p1.next, p2.next)
    elif(p1 != None and ((p2 != None and p1.power < p2.power) or p2 == None)):
        ptr.coeff = p1.coeff
        ptr.power = p1.power
        ptr.next = pAdd(p1.next, p2)
    elif(p2 and ((p1 != None and p1.power > p2.power) or p1 == None)):
        ptr.coeff = p2.coeff
        ptr.power = p2.power
        ptr.next = pAdd(p1,p2.next)
    else:
        return None
    return ptr

def pInsertOrAdd(p, ptr):
    # p->next anytime contains a partial product.
    # add ptr at appropriate place in it keeping powers in order.
    prev = p
    curr = prev.next
    while(curr != None and curr.power < ptr.power):
        prev = curr
        curr = curr.next
    if(curr != None and curr.power == ptr.power):
        curr.coeff += ptr.coeff
    else:
        prev.next =ptr
        ptr.next = curr
    return p

def pMult(p1, p2):
    ptr1 = p1
    p3 = node()
    while(ptr1 != None):
        ptr2 = p2
        while(ptr2 != None):
            ptr = node()
            ptr.coeff = ptr1.coeff * ptr2.coeff
            ptr.power = ptr1.power + ptr2.power
            p3 = pInsertOrAdd(p3, ptr)
            ptr2 = ptr2.next
        ptr1 = ptr1.next
    return p3.next

def pEval(p1, x):
    result = 0
    ptr = p1
    while(ptr != None):
        result += ptr.coeff * pow(x, ptr.power)
        ptr = ptr.next
    return result

def main():
    p1 = createPoly(3, "3 5 -1 3 -10 0")
    p2 = createPoly(3, "-2 3 0 2 20 0")
    pPrint(p1)
    pPrint(p2)
    pPrint(pAdd(p1, p2))
    pPrint(pSub(p1, p2))
    #print("till here ok")
    pPrint(pMult(p1,p2))
    print("Value of p1 at x= 2 is " + str(pEval(p1,2)))


main()
