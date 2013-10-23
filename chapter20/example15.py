#Chapter 20.15
# MERGING OF TWO CIRCULAR LISTS

class node:  # Node class

    def __init__(self):
        self.data = 0
        self.link = None

def insert(p, n):  # INsert Function
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



def printlist(p):  # Function to print the list
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


def reverselist(p):  # Function to reverse the list
    prev = None
    if(p != None):
        curr = p
        temp = curr
        while(curr.link != p):
            curr = curr.link
            temp.link = prev
            prev = temp
            temp = curr
        temp.link = prev
        p.link = temp
        p = temp
    return(p)

def main():  #Main Function
    start = None
    print("Enter the number of nodes")
    n = int(raw_input())
    while(n > 0):
        print("Enter the data values to be placed in the node")
        x = int(raw_input())
        start = insert(start, x)
        n = n - 1
    print("The list created is")
    printlist(start)
    start1 = reverselist(start)
    print("The reversed list is")
    printlist(start1)


main()