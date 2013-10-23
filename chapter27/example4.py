# Chapter 27.4
#  IMPLEMENTATION OF A SET USING A BINARY TREE

N = 100

class node:

    def __init__(self):
        self.val = 0
        self.parent = 0

global sets
sets = [node() for i in range(N)] # all sets are contained in it.
setsindex = 0 # total no of elements in sets.

def insertRoot(val):
    # insert val in sets as a root of a new tree.
    global sets
    global setsindex
    sets[setsindex].val = val
    sets[setsindex].parent = -1
    setsindex = setsindex + 1
    return setsindex - 1

def insertElement(rootindex, val):
    #insert element val in set whose root is indexed at rootindex.
    global sets
    global setsindex
    sets[setsindex].val = val
    sets[setsindex].parent = rootindex
    setsindex = setsindex + 1

def buildSet(a, n):
    """
    /*
     * repeated calls to this fun with diff arrays will insert diff set in sets.
     * forms a tree representation of elements in a.
     * n is number of elements in the set.
     * empty set(n==0) cannot be represented here.
     * returns index of root.
     */
"""
    global setsindex
    if(n <= 0):
        print("n should be > 0")
        return -1
    if(setsindex+n > N):
        print("overflow")
        return -1
    # a[0] becomes the root
    rootindex = insertRoot(a[0])
    for i in range(1,n):
        insertElement(rootindex, a[i])
    return rootindex

def PrintSets():
    print("\n")
    for i in range(setsindex):
        print(sets[i].val),
        print(sets[i].parent)
    print("\n")

def unionSets(rindex1, rindex2):
    # makes a union of sets whose root indices are rindex1 and rindex2
    global sets
    sets[rindex2].parent = rindex1
    return rindex1

def findSet(valindex):
    # given a val at index valindex in the array, finds index of its root
    global sets
    while(sets[valindex].parent != -1 ):
        valindex=sets[valindex].parent
    return valindex

def getIndex(val):
    # dummy procedure to return index in array of val
    for i in range(setsindex):
        if(sets[i].val == val):
            return i
    return -1

def main():
    global sets
    s1 = [1,7,8,9]
    s2 = [5,2,10]
    s3 = [3,4,6]
    i1 = buildSet(s1, 4)
    i2 = buildSet( s2, 3 )
    i3 = buildSet( s3, 3 )
    i1 = unionSets(i1, i2)
    print("3 " + str(sets[findSet( getIndex(3) )].val ))
    print("5 " + str(sets[findSet( getIndex(5) )].val ))
    print("2 " + str(sets[findSet( getIndex(2) )].val ))
    i1 = unionSets(i3, i1)
    print("3 " + str(sets[findSet( getIndex(3) )].val ))
    print("5 " + str(sets[findSet( getIndex(5) )].val ))
    print("2 " + str(sets[findSet( getIndex(2) )].val ))
    PrintSets()

main()


