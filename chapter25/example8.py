# Chapter 25.8
#  COMPUTE N EQUIVALENCE CLASSES

class node:

    def __init__(self):
        self.val = None
        self.next = None

def getList(a, n):
    # from a list of N integers
    List = None
    for i in range(n):
        ptr = node()
        ptr.val = a[i]
        ptr.next= List
        List = ptr
    return List

def applyMod(List, n):
    # apply (mod n) on every element of list and store that element in
    # the list modlists[(mod n)].
    # thus we form array[n] of lists
    # each list is one equivalence class
    modlists = [node() for i in range(n)]
    ptr = List
    if(ptr != None):
        Next =ptr.next
    else:
        Next = None
    while(ptr != None):
        ptr.next = modlists[ptr.val % n]
        modlists[ptr.val % n] = ptr
        ptr = Next
        if(Next != None):
            Next = Next.next
        else:
            Next = None
    return modlists

def printModlists(modlists, n):
    # prints the equivalence classes
    for i in range(n):
        print(i),
        print(": "),
        ptr = modlists[i]
        while(ptr != None and ptr.val != None):
            print(ptr.val),
            ptr = ptr.next
        print("\n")
    print("\n")

def main():
    a = [10,2,3,44,432,35,6576,34,12,5456,23423,234,23]
    List = getList(a,len(a))
    print("Enter the number of equivalence classes: ")
    #n = int(raw_input())  input
    n = 5
    modlists = applyMod(List, n)
    printModlists(modlists, n)

main()
