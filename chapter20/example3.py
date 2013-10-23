#Chapter 20.3
# SORTING AND REVERSING A LINKED LIST

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


def reverse(p):  # Function to reverse the list
    prev = None
    curr = p
    while(curr!= None):
        p = p.link
        curr.link = prev
        prev = curr
        curr = p
    return prev


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
    start = reverse(start)
    print("The reverse List is")
    printlist(start)


main()  #  Main Function

