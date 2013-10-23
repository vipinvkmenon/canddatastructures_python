#Chapter 23.7
# IMPLEMENTATION OF REHASHING

MAXLEN = 80
HASHSIZE = 23             # some prime val.

class node():
    def __init__(self,vl,ky):
        self.val = vl
        self.key = ky

def hGetIndex1(key):
    # returns index into hashtable applying hash function.
    # uses sum of elements followed by mod function for hashing.
    keyptr = key
    n = 0
    for j in range(len(keyptr)):
        n += ord(keyptr[j])
    return (n % HASHSIZE)

def hGetIndex2(key):
    # returns index into hashtable applying hash function.
    # sums the products of elements with their indices and then mod.
    n = 0
    print("Function 2:).\n")
    keyptr = key
    i = 1
    for j in range(len(keyptr)):
        n += i * ord(keyptr[j])
        i = i + 1
    return n % HASHSIZE

def hGetEmptySlot(h, index):
    # search for an empty slot in h starting from index+1.
    for i in range(index + 1, HASHSIZE):  # index+1 to end of hashtable.
        if(h[i] == None):
            return i
        for i in range(index):  # tarting from 0 to index 1.
            if(h[i] == None):
                return i
    return -1

def hLinearProbe(h, key, index):
    # search for node having key in h starting from index+1.
    for i in range(index + 1, HASHSIZE):
        if(h[i] and h[i] == key):
            return i
        elif(h[i] == None):
            return -1
    for i in range(index):
        if(h[i] and h[i] == key):
            return i
        elif(h[i] == None):
            return -1
    return -1

def hInsert(h, key, val):
    # insert s in hashtable h.
    # does NOT check for duplicate insertion.
    ptr = node(0,"")
    index = hGetIndex1(key)
    if(h[index] != None):
        index = hGetIndex2(key)
        if(h[index] != None):
            index = hGetEmptySlot(h, index)
            if(index == -1):
                print("Error: Hashtable full")
                return 0
    ptr.key = key
    ptr.val = val
    h[index] = ptr
    print("h[" + str(index) + "] = " + key)
    return h

def hGetVal(h, key):
    index = hGetIndex1(key)
    if(h[index] and (h[index].key != key)):
        index = hGetIndex2(key)
        if(h[index] and (h[index].key == key)):
            index = hLinearProbe(h, key, index)
            if(index == -1):
                return -1
        elif(h[index] == None):
            return -1
    elif(h[index] == None):
        return -1
    print("index = " + str(index))
    return h[index].val

def printHash(h):
    # print the hashtable.
    for i in range(HASHSIZE):
        if(h[i] != None):
            print(i),
            print(h[i].key +" = " + str(h[i].val)),
            print("\n")

def main():
    i = 0
    g = "abc"
    h = []
    for i in range(len(g)):
        h.append(node(i,g[i]))
    for i in range(20):
        h.append(None)
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
    printHash(h)


main()
