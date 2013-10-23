#Chapter 21.5
# SEARCHING FOR A TARGET KEY IN A BINARY SEARCH TREE

class tnode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

# Function to get a pointer to the node data value is given as well as the
# to its root
def getptr(p, key, y):
    if(p == None):
        return(None)
    temp = p
    y = None
    while(temp != None):
        if(temp.data == key):
            return(temp, y)
        else:
            y = temp # Store pointer at root
            if(temp.data > key):
                temp = temp.lchild
            else:
                temp = temp.rchild
    return(None, y)


# A fuction to delete the node whose data value is given
def delete(p, val):
    x = None
    y = None
    x,y = getptr(p, val, y)
    if (x == None):
        print("Node does not exist")
        return(p)
    else:
        if(x == p):  # To delete root node
            temp = x.lchild
            y = x.rchild
            p = temp
            while(temp.rchild != None):
                temp = temp.rchild
            temp.rchild = y
            return(p)
        if((x.lchild != None) and (x.rchild != None)):  # To delete node with both children
            if(y.lchild == x):
                temp = x.lchild
                y.lchild = x.lchild
                while(temp.rchild != None):
                    temp = temp.rchild
                x.lchild = None
                x.rchild = None
            else:
                temp = x.rchild
                y.rchild = x.rchild
                while(temp.lchild != None):
                    temp = temp.lchild
                x.lchild = None
                x.rchild = None
            return(p)
        if(x.lchild == None and x.rchild != None): # to delete node with one child
            if(y.lchild == x):
                y.lchild = x.rchild
            else:
                y.rchild = x.rchild
            x.rchild = None
            return(p)
        if(x.lchild != None and x.rchild == None):
            if(y.lchild == x):
                y.lchild = x.lchild
            else:
                y.rchild = x.lchild
            x.lchild = None
            return(p)
        if((x.lchild == None) and (x.rchild == None)): # delete node with no child
            if(y.lchild == x):
                y.lchild = None
            else:
                y.rchild = None
            return(p)


def inorder1(p):  # iterative printing
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


def insert(p, val):  # insert node function
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
    print("\nEnter the value to be deleted")
    n = int(raw_input())
    root = delete(root, n)
    print("Tree after deletion")
    inorder1(root)



main()
