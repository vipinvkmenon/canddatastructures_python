#Chapter 20.12
# CIRCULAR LINKED LISTS

class node:

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

def main():  # Main function
    start = None
    print("Insert the number of nodes to be created")
    n = int(raw_input())
    while(n > 0):
        print("Enter the values")
        values = int(raw_input())
        start = insert(start,values)
        n = n - 1
    print("The created list is")
    printlist(start)



main()  # Main function entery
