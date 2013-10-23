# Chapter 20.9
# MERGING OF TWO SORTED LISTS

class node:  # Node class

    def __init__(self):
        self.data = 0
        self.link = None

def insert(p, n):  # Insert function
    if(p ==None):
        p = node()
        if(p == None):
            print("Error")
            exit()
        p.data = n
    else:
        p.link = insert(p.link, n)
    return(p)


def printlist(p):  #printlist
    print("The data values in the list are\n")
    while(p !=None):
        print(p.data)
        p = p.link

def erase(p, free):
    temp = p
    while(temp.link != None):
        temp = temp.link
    temp.link = free
    free = p
    p = None
    return p, free

def main():  # Main Function
    free = None
    start = None
    print("Enter the nodes in initial first list") # this code will create a free list for the test purpose
    n = int(raw_input())
    while(n > 0):
        print("Enter the data values to be placed in a node")
        x = int(raw_input())
        free = insert(free, x)
        n = n -1
    print("The first list is")
    printlist(free)

    print("Enter the nodes in a node") # this code will create a list to be erased
    n = int(raw_input())
    while(n > 0):
        print("Enter the values")
        x = int(raw_input())
        start = insert(start, x)
        n = n - 1
    print("The first list is")
    printlist(start)
    print("The free list islist is:")
    printlist(free)
    print("The list to be erased is:")
    printlist(start)
    start, free = erase(start, free)
    print("The free list after adding all the nodes from the list to be erased is:")
    printlist(free)


main()
