# Chapter 20.8
# MERGING OF TWO SORTED LISTS

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


def sortlist(p):  # Function to list sort
    q = None
    while(p != None):
        prev = None
        Min = p
        temp1 = p
        temp2 = p.link
        while(temp2 != None):
            if(Min.data > temp2.data):
                Min = temp2
                prev = temp1
            temp1 = temp2
            temp2 = temp2.link
        if(prev == None):
            p = Min.link
        else:
            prev.link = Min.link
        Min.link = None
        if(q == None):
            q = Min
        else:
            temp1 = q
            while(temp1.link != None):
                temp1 = temp1.link
            temp1.link = Min
    return(q)

def merge(p, q):  # Merge function
    r= None
    if(p == None):
        r = q
    else:
        if(q == None):
            r = p
        else:
            if(p.data < q.data):
                r = p
                temp = p
                p = p.link
                temp.link = None
            else:
                r = q
                temp = q
                q = q.link
                temp.link = None
            while((p !=None) and (q != None)):
                if(p.data < q.data):
                    temp.link = p
                    p = p.link
                    temp = temp.link
                    temp.link = None
                else:
                    temp.link = q
                    q = q.link
                    temp = temp.link
                    temp.link = None
                if(p != None):
                    temp.link = p
                if(q != None):
                    temp.link = q
    return(r)

def main():  # Main Function
    start1 = None
    start2 = None
    start3 = None
    print("Enter the nodes in first list")
    n = int(raw_input())
    while(n > 0):
        print("Enter the values")
        x = int(raw_input())
        start1 = insert(start1, x)
        n = n -1
    print("The first list is")
    printlist(start1)
    start1 = sortlist(start1)
    print("The sorted list is")
    printlist(start1)
    print("Enter the nodes in second list")
    n = int(raw_input())
    while(n > 0):
        print("Enter the values")
        x = int(raw_input())
        start2 = insert(start2, x)
        n = n -1
    print("The first list is")
    printlist(start2)
    start2 = sortlist(start2)
    printlist(start2)
    start3 = merge(start1, start2)
    printlist(start3)


main() # Main function ENtry

