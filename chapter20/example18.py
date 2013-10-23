#Chapter 20.18
# DELETE A NODE IN A DOUBLY LINKED LIST

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

def delete(p, node_no, val):
    prev = None
    if((node_no < 0) or (node_no > nodecount(p))):
        print("Error ! the specified node does not exist")
        exit()
    if((node_no == 0) or (node_no == 1)):
        temp = p
        p = temp.right
        p.left = None
        val = temp.data
        return p, val
    else:
        temp = p
        i = 1
        while(i < node_no):
            i = i + 1
            prev = temp
            temp = temp.right
        prev.right = temp.right
        if(temp.right != None):
            temp.right.left = prev
            val = temp.data
        return p, val

def main():
    start = None
    end = None
    print("Enter the nodes to be created")
    n = int(raw_input())
    while(n > 0):
        print("Enter the data to be placed in the node")
        x = int(raw_input())
        start, end = insert(start, end, x)
        n = n - 1
    print("The list created is")
    printfor(start)
    print("Enter the number of the node to be deleted")
    n = int(raw_input())
    start, x = delete(start, n, x)
    print("the data value of the node deleted is " + str(x))
    print("The  list after the deletion is")
    printfor(start)


main()