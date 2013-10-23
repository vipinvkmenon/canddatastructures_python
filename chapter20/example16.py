#Chapter 20.16
# DOUBLY LINKED LISTS

class dnode:

    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None

def insert(p, q, n):
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

def printfor(p):
    print("The values in the forward order are")
    while(p != None):
        print(str(p.data) + str("\t")),
        p = p.right
    print("\n")

def printrev(p):
    print("The values in the reverse order are")
    while(p != None):
        print(str(p.data) + str("\t")),
        p = p.left
    print("\n")

def main():
    start = None
    end = None
    print("Enter the nodes to be created")
    n = int(raw_input())
    while(n > 0):
        print("Enter the data values to be placed")
        x = int(raw_input())
        start, end = insert(start, end, x)
        n = n -1
    print("The created list is")
    printfor(start)
    printrev(end)

main()
