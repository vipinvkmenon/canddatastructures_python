#Chapter 21.4
# SEARCHING FOR A TARGET KEY IN A BINARY SEARCH TREE

class tnode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def search(p, key):
    temp = p
    while(temp != None):
        if(temp.data == key):
            return(temp)
        else:
            if(temp.data > key):
                temp = temp.lchild
            else:
                temp = temp.rchild
    return(None)


def inorder1(p):
    stack = [None for i in range(100)]
    top = -1
    if(p != None):
        top = top + 1
        stack[top] = p
        p = p.lchild
        while(top >= 0):
            while(p != None):
                top = top + 1
                stack[top] = p
                p = p.lchild
            p = stack[top]
            top = top - 1
            print(str(p.data) +"\t")
            p = p.rchild
            if(p != None):
                top = top + 1
                stack[top] = p
                p = p.lchild




def insert(p, val):
    if(p == None):
        p = tnode()
        if(p == None):
            print("Cannot allocate")
            exit()
        p.data = val
    else:
        temp1 = p
        while(temp1 != None):
            temp2 = temp1
            if(temp1.data >= val):
                temp1 = temp1.lchild
            else:
                temp1 = temp1.rchild
        if(temp2.data >= val):
            temp2.lchild = tnode()
            temp2 = temp2.lchild
            if(temp2 == None):
                print("Cannot allocate")
                exit()
            temp2.data = val
        else:
            temp2.rchild = tnode() # inserts new node to kleft
            temp2 = temp2.rchild
            if(temp2 == None):
                print("Cannot allocate")
                exit()
            temp2.data = val
    return(p)


def main():  # Main function
    root = None
    print("Enter the number of nodes")
    n = int(raw_input())
    while(n > 0):
        print("Enter the data value")
        x = int(raw_input())
        root = insert(root, x)
        n = n - 1
    print("The values are")
    inorder1(root)
    print("\nEnter the value ")
    n = int(raw_input())
    temp = search(root, n)
    if(temp != None):
        print("\nThe data value is present in the tree")
    else:
        print("\nThe data is not present")


main()
