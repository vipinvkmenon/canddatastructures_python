#Chapter 20.14
# MERGING OF TWO CIRCULAR LISTS

class node:  # Node class

    def __init__(self):
        self.data = 0
        self.link = None

def insert(p, n):
    temp = node()
    if(p == None):
        p = node()
        if(p == None):
            print("Error")
            exit()
        p.data = n
        p.link = p
    else:
        temp = p
        while(temp.link != p):
            temp = temp.link
        temp.link = node()
        if(temp.link == None):
            print("Error")
            exit()
        temp = temp.link
        temp.data = n
        temp.link = p
    return(p)



def printlist(p):
    temp = p
    print("The data values in the list are\n")
    if(p != None):
        print(temp.data)
        temp = temp.link
        while(temp != p):
            print(temp.data)
            temp = temp.link
    else:
        print("The list is empty")


def merge(p, q):  # Merge Function
    temp = None
    r = None
    r = p
    temp = p
    while(temp.link != p):
        temp = temp.link
    temp.link = q
    temp = q
    while(temp.link != q):
        temp = temp.link
    temp.link = r
    return(r)

def main():
    start1 = None
    start2 = None
    start3 = None
    print("Enter the number of nodes")
    n = int(raw_input())
    while(n > 0):
        print("Enter the data values to be placed in the node")
        x = int(raw_input())
        start1 = insert(start1, x)
        n = n - 1
    print("The list created is")
    printlist(start1)
    print("Enter the data value of n")
    n = int(raw_input())
    while(n > 0):
        print("Enter the data values to be placed in the node")
        x = int(raw_input())
        start2 = insert(start2, x)
        n = n - 1
    print("The list created is")
    printlist(start2)
    start3 = merge(start1, start2)
    print("The resultant list is")
    printlist(start3)


main()