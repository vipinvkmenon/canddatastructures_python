#Chapter 20.13
# SPLITTING A LIST WITH 2N NODES INTO TWO SEPARATE AND EQUAL LISTS


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

def split(p, q, n):
    temp = p
    i = 1
    while(i < n):
        temp = temp.link
        i = i + 1
    q = temp.link
    print(q.data)
    temp.link = p
    temp = q
    while(temp.link != p):
        temp = temp.link
    temp.link = q
    return p, q

def main():
    start =None
    start1 =None
    print("Enter the data value of n")
    n = int(raw_input())
    num = n
    n = n * 2
    while(n > 0):
        print("Enter the data values to be placed in the node")
        x = int(raw_input())
        start = insert(start, x)
        n = n - 1
    print("The list created is")
    printlist(start)
    start, start1 = split(start, start1, num)
    print("The second list is")
    printlist(start1)

main()