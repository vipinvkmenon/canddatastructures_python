#Chapter 20.2
# INSERTING A NODE BY USING RECURSIVE PROGRAMS


class node:
    def __init__(self):
        self.data = 0
        self.link = None

def insert(p, n):  # Inert function
    if(p ==None):
        p = node()
        if(p == None):
            print("Error")
            exit()
        p.data = n
    else:
        p.link = insert(p.link, n)
    return(p)


def printlist(p):  # Print list function
    print("The data values in the list are\n")
    while(p !=None):
        print(p.data)
        p = p.link

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


