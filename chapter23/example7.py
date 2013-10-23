#Chapter 23.7
# IMPLEMENTATION OF A HASH SEARCH

MAXLEN = 80
HASHSIZE = 23             # some prime val.
SHIFTBY = 3

class node():

    def __init__(self,vl,ky):
        self.val = vl
        self.key = ky
        self.next = None

hashtable = [node(0,"") for i in range(HASHSIZE)]

def hGetIndex(key):
    # returns index into hashtable applying hash function.
    # uses shift-folding followed by mod function for hashing.
    finaln = 0
    keyptr = key
    t = 0
    while(t < len(keyptr)):
        i = 0
        n = 0
        j = 0
        while(i < SHIFTBY and j < len(keyptr)):
            n = n * 10 + ord(keyptr[j])
            i = i + 1
            j = j + 1
        finaln += n
        t += 1
    finaln %= HASHSIZE
    return finaln

def hInsert(h, key, val):
    # insert s in hashtable h.
    # use shift-folding followed by mod function for hashing.
    # does NOT check for duplicate insertion.
    ptr = node(0,"")
    index = hGetIndex(key)
    ptr.key = key
    ptr.val = val
    ptr.next = h[index]
    h[index] = ptr
    print("h[" + str(index) + "] = " + key)
    return h

def hGetVal(h, key):
    # returns val corresponding to key if present in h else -1
    ptr = h[hGetIndex(key)]
    while(ptr != None and ptr.key != key):
        ptr = ptr.next
    if(ptr != None):
        return ptr.val
    return -1

def printHash(h):
    # print the hashtable rowwise.
    for i in range(HASHSIZE):
        print(i),
        ptr = h[i]
        while(ptr != None):
            print(ptr.key + " = " + str(ptr.val)),
            ptr = ptr.next
        print("\n")

def main():
    i = 0
    g = "abc"
    h = []
    for i in range(len(g)):
        h.append(node(i,g[i]))
    for i in range(20):
        h.append(node(0,""))
    print("Enter the string to be hashed:")
    s = raw_input()
    while(s != ""):
        h = hInsert(h, s, i)
        i = i + 1
        s = raw_input()
    print("Enter the string to be searched")
    s = raw_input()
    while(s != ""):
        print(s + " was inserted at number " + str(hGetVal(h, s)))
        print("Enter the string to be searched(enter to end): ")
        s = raw_input()
    # printHash(h)


main()




