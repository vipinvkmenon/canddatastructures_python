#Chapter 20.4
# Delete from singly linked list

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


def length(p):  # Find lengt of the linked list
    count = 0
    while(p != None):
        count = count + 1
        p = p.link
    return(count)

def delet(p, node_no):  # a function to delete the specified node
    if(p == None):
        print("There is no node to be deleted")
    else:
        if(node_no > length(p)):
            print("Error")
        else:
            prev = None
            curr = p
            i = 1
            while(i < node_no):
                prev = curr
                curr =curr.link
                i = i + 1
            if(prev == None):
                p = curr.link
            else:
                prev.link = curr.link
    return(p)

def main():  # main function
    start = None
    print("ENter nodes to be created")
    n = int(raw_input())
    while(n > 0):
        print("Enter the values to be inserted")
        x = int(raw_input())
        start = insert(start, x)
        n = n - 1
    print("The list before deletion")
    printlist(start)
    print("Enter node no")
    n = int(raw_input())
    start = delet(start, n)
    print("The list after deletion is")
    printlist(start)

main()