# Chapter 20.10
# POLYNOMIAL REPRESENTATION

class pnode:  # Node class

    def __init__(self):
        self.exp = 0
        self.coeff = 0
        self.link = None

def insert(p, e, c):  # Insert function
    if(p == None):
        p = pnode()
        if(p == None):
            print("Error")
            exit()
        p.coeff = c
        p.exp = e
    else:
        p.link = insert(p.link, e, c)
    return(p)

def sortlist(p):  # Function to list sort
    q = None
    while(p != None):
        prev = None
        Max = p
        temp1 = p
        temp2 = p.link
        while(temp2 != None):
            if(Max.exp < temp2.exp):
                Max = temp2
                prev = temp1
            temp1 = temp2
            temp2 = temp2.link
        if(prev == None):
            p = Max.link
        else:
            prev.link = Max.link
        Max.link = None
        if(q == None):
            q = Max  # Moves the node with highest data value
        else:
            temp1 = q
            while(temp1.link != None):
                temp1 = temp1.link
            temp1.link = Max
    return(q)

def polyadd(p,q):  # Add the polynomials
    r = None
    while((p != None) and (q != None)):
        if(p.exp > q.exp):
            r = insert(r,p.exp, p.coeff)
            p = p.link
        else:
            if(p.exp < q.exp):
                r = insert(r, q.exp, q.coeff)
                q = q.link
            else:
                c = p.coeff + q.coeff  # Add coefficients
                e = q.exp
                r = insert(r, e, c)
                p = p.link
                q = q.link
    if(p != None):
        r = insert(r, p.exp, p.coeff)
        p = p.link
    while(q != None):
        r = insert(r, q.exp, q.coeff)
        q = q.link
    return(r)

def printlist(p):  #printlist
    print("The polynomial is\n")
    while(p !=None):
        print(str(p.exp) + " " + str(p.coeff))
        p = p.link

def main():  # Main Function
    poly1= None
    poly2 = None
    print("Enter the terms in polynomial1")
    n = int(raw_input())
    while(n > 0):
        print("Enter the exponent and coefficient of the term number")
        e = int(raw_input())
        c = float(raw_input())
        poly1 = insert(poly1, e, c)
        n = n -1
    print("Enter the terms in polynomial2")
    n = int(raw_input())
    while(n > 0):
        print("Enter the exponent and coefficient of the term number")
        e = int(raw_input())
        c = float(raw_input())
        poly2 = insert(poly2, e, c)
        n = n - 1
    poly1 = sortlist(poly1)  # Sort the list
    poly2 = sortlist(poly2)
    print("The polynomial1 is")
    printlist(poly1)
    print("The polynomial2 is")
    printlist(poly2)
    result = polyadd(poly1, poly2)
    print("The result is")
    printlist(result)

main()
