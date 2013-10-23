#Chapter 21.1
# BINARY SEARCH TREE

class tnode:
    def __init__(self):
        self.data = 0
        self.lchild = None
        self.rchild = None


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


def inorder(p):  # Inorder function
    if(p != None):
        inorder(p.lchild)
        print p.data
        inorder(p.rchild)
    return p

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
    inorder(root)

main()
