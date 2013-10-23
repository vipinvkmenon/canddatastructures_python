# Chapter 20.7
# COUNTING THE NUMBER OF NODES OF A LINKED LIST

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

def nodecount(p):  # Find lengt of the linked list
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
    n = nodecount(start)
    print("The number of nodes in a list are: " + str(n))

main() # Main function Entry