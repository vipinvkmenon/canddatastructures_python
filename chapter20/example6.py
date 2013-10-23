# Chapter 20.6
# INSERTING A NEW NODE IN A SORTED LIST

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


def sortlist(p):  # Function to list sort
    q = None
    while(p != None):
        prev = None
        Min = p
        temp1 = p
        temp2 = p.link
        while(temp2 != None):
            if(Min.data > temp2.data):
                Min = temp2
                prev = temp1
            temp1 = temp2
            temp2 = temp2.link
        if(prev == None):
            p = Min.link
        else:
            prev.link = Min.link
        Min.link = None
        if(q == None):
            q = Min
        else:
            temp1 = q
            while(temp1.link != None):
                temp1 = temp1.link
            temp1.link = Min
    return(q)

def sinsert(p, n):
    curr = p
    prev = None
    while(curr.data < n and curr.link != None):
        print(curr.data)
        prev = curr
        curr = curr.link
    if(curr.data < n and curr.link == None):
        prev = curr
        curr = curr.link
    if(prev == None):
        curr = node()
        if(curr == None):
            print("Error cannot allocate")
            exit()
        curr.data = n
        curr.link = p
        p = curr
    else:
        curr = node()
        curr.data = n
        curr.link = prev.link
        prev.link = curr
    return(p)


def length(p):  # Find lengt of the linked list
    count = 0
    while(p != None):
        count = count + 1
        p = p.link
    return(count)



def main():
    start = None
    print("Enter the nodes")
    n = int(raw_input())
    while(n > 0):
        print("Enter the data values to be placed in a node\n")
        x = int(raw_input())
        start = insert(start, x)
        n = n - 1
    print("The created list is")
    printlist(start)
    print("The sorted list")
    start = sortlist(start)
    printlist(start)
    print("Enter value to be inserted")
    n = int(raw_input())
    start = sinsert(start, n)
    print("The list after insertion is")
    printlist(start)


main()  #  Main Function

