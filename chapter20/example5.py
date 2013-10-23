#Chapter 20.5
# INSERTING A NODE AFTER THE SPECIFIED NODE IN A SINGLY LINKED LIST

class node:  # Node class

    def __init__(self):
        self.data = 0
        self.link = None

def insert(p, n):  # function which appends a new node to an existing list used for building a list
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

def newinsert(p, node_no, value):

    if(node_no < 0 or node_no > length(p)):
        print("Error! specified node does not exist")
        exit()
    if(node_no == 0):
        temp = node()
        if(temp == None):
            print("Cannot Allocate")
            exit()
        temp.data = value
        temp.link = p
        p = temp
    else:
        temp = p
        i = 1
        while(i < node_no):
            i = i + 1
            temp = temp.link
        temp1= node()
        if(temp == None):
            print("Error. Cannot allocate")
            exit()
        temp1.data = value
        temp1.link = temp.link
        temp.link = temp1
    return(p)

def length(p):  # Find lengt of the linked list
    count = 0
    while(p != None):
        count = count + 1
        p = p.link
    return(count)


def main():
    start = None
    print("Enter nodes to be created")
    n = int(raw_input())
    while(n > 0):
        print("Enter the values")
        x = int(raw_input())
        start = insert(start, x)
        n = n - 1
    print("The node before insertion is")
    printlist(start)
    print("Enter the node adter which insertion needs to be done")
    n = int(raw_input())
    print("Enter the value")
    x = int(raw_input())
    start = newinsert(start, n, x)
    print("The list after insertion is")
    printlist(start)

main()  # Main Function ENtry


