# Chapter 19.3
# CONVERT AN INFIX EXPRESSION TO PREFIX FORM

# -----------------------------------------
class node:
    data = 0
    link = 0
# -----------------queue implement -----------

global front  # Global ariable
front = None
global g
g = 0

def qempty(rear):  # To check if queue empty
    if (rear == None or rear == 0):
        return 1
    else:
        return 0


def qpop(rear):  # Pop from Queue
    global front
    try:
        if((front == rear) and (rear == None)):
            print("The queue is empty cannot delete Error\n")
            # exit()
        value = front.data
        temp = front
        front =front.link
        if(rear == temp):
            rear = rear.link
    except:
        print(" exception The queue is empty cannot delete Error\n")
        print(qempty(rear))
        # exit()
    return rear, value

def qpush(rear, value):  # pushvalue to queue
    temp = node()  # Create a new node using data value passed
    global front
    try:
        temp.data = value
        temp.link = None
        if(rear == None):
            rear = temp
            front = rear
        else:
            rear.link = temp
            rear = temp
    except:
        print("The stack is empty can not pop Error")

    return rear

# --------------Stack Implementation---------------

def spush(p, value):  # push to stack
    temp = node()  # Create new node
    try:
        temp.data = value
        temp.link = p
        p = temp
    except:
        print("The stack is empty can not pop Error")

    return(p)
def spop(p):   # pop from stack

    try:
        value = p.data
        p = p.link
        return p, value
    except:
        print("The stack is empty can not pop Error")


def sempty(rear):  # to check if stack empty
    if (rear == 0):
        return 1
    else:
        return 0

def stop(p):  #stack top

    try:
        value = p.data
        return value
    except:
        print("The stack is empty can not pop Error")


#----------------------Main program --------------------------

N = 80
FALSE = 0
TRUE =1
NOPS = 7
operators = ["(",")","^","/","*","+","-"]
priorities = [4,4,3,2,2,1,1]
associates = ["R","L","L","L","L","L","L"]
global tptr
tptr = [0 for i in range(N)]
z = 0

 # tptr = t   # this is where prefix will be saved.

def getIndex(op):  # returns index of operatior
    for i in range(NOPS):
        if(operators[i] ==op):
            return i
    return -1

def getPriority(op): # Returns priority
    return priorities[getIndex(op)]

def getAssociativity(op):  # returns associativity
    return associates[getIndex(op)]

def isop(op):  # is an operator
    return (getIndex(op) != -1)

def isalpha(alp):
    if((ord(alp) <= 57 and ord(alp) >= 48) or (ord(alp) <= 90 and ord(alp) >= 65) or (ord(alp) <= 122 and ord(alp) >= 97)):
        return 1
    return 0


def processop(op, q, s):  # process operator
    global g
    global tptr
    if(op == ")"):
        s = spush(s, op)
    elif(op == "("):
        while(qempty(q) == 0):
            q, tptr[g] = qpop(q)
            g = g + 1
    else:
        while(sempty(s) == 0):
            priop = getPriority(op)
            topop = stop(s)
            pritop = getPriority(topop)
            asstop = getAssociativity(topop)
            if((pritop < priop) or (pritop == priop and asstop == "L") or topop == ")"):
                break
            while(qempty(q) == 0):
                q, tptr[g] = qpop(q)
                g = g + 1
            s, tptr[g] = spop(s)
            g = g + 1
        print("S pushing....")
        s = spush(s, op)
    return q, s

def in2pre(Str):  # infix to prefix
    q = None
    s = node()
    resptr = []
    global tptr
    # tptr = t
    global g
    for m in Str:
        if(isalpha(m) == 1):
            q = qpush(q, m)
        elif(isop(m) == 1):
           print("process op")
           q, s = processop(m, q, s)
    while(qempty(q) == 0):
        q, tptr[g] = qpop(q)
        g = g + 1
    while(sempty(s) == 0):
        s, tptr[g] = spop(s)
        # tptr.append(apps)
        #print("S popping  177 " + str(tptr[g]))
        g = g + 1
    tptr[g] = 0
    for k in range(N):
        resptr.append(tptr[k])
    resptr.append(0)
    return resptr


def main():
    # s = [0 for x in range(N)]
    print("enter infix freespaces max 80")
    s = raw_input()
    respt = in2pre(s)
    for z in range(len(s)):
        print(respt[z]),
    print("\n")

main()  # Main function entry



