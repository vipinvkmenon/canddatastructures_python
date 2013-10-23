#Chapter 20.17
# INSERTION OF A NODE IN A DOUBLY LINKED LIST

class dnode:  # node class

    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None

def insert(p, q, n):  # inser nodes
    if(p == None):
        p = dnode()
        if(p == None):
            print("Error")
            exit
        p.data = n
        q = p
    else:
        temp = dnode()  # Create new node
        if(temp == None):
            print("Error")
            exit
        temp.data = n
        temp.left = q
        q.right = temp
        q= temp
    return p, q

def printfor(p):  # print nodes
    print("The values in the forward order are")
    while(p != None):
        print(str(p.data) + str("\t")),
        p = p.right
    print("\n")

def nodecount(p):  # count number of nodes
    count = 0
    while(p != None):
        count = count + 1
        p = p.right
    return count


def newinsert(p, node_no, value):  # Insert new node
    if(node_no < 0):
        print("Specified node does not exist")
        exit()
    if(node_no > nodecount(p)):
        print("Specified node does not exist")
        exit()
    if(node_no == 0):
        temp = dnode()
        if(temp == None):
            print("Error cannot allocate")
            exit()
        temp.data = value
        temp.right = p
        p = temp
    else:
        temp = p
        i = 1
        while(i < node_no):
            i = i + 1
            temp = temp.right
        print("calue at node here" + str(temp.data))
        temp1 = dnode()
        if(temp1 == None):
            print("Error cannot allocate")
            exit
        temp1.data = value
        temp1.right = temp.right
        temp1.left = temp
        temp1.left.right = temp1
        if(temp1.right != None):
            temp1.right.left = temp1

    return(p)

def main():
    start = None
    end = None
    print("Enter the nodes to be created")
    n = int(raw_input())
    while(n > 0):
        print("Enter the data value to be placed")
        x = int(raw_input())
        start, end = insert(start, end, x)
        n = n - 1
    print(nodecount(start))
    print("Enter the node number after which new node to be placed")
    n = int(raw_input())
    print("Enter the data to be placed in the node")
    x = int(raw_input())
    start = newinsert(start, n, x)
    printfor(start)

main()
