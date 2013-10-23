# Chapter 25.2
# IMPLEMENTATION OF CIRCULAR LISTS BY USING ARRAYS

N = 10 # size of the list.
FIRSTINDEX = 0  # index of first element in the list.
ILLEGALINDEX = -1  # illegal index - for special cases.
SUCCESS = 0  #  success code.
EINDEXOUTOFBOUND = -1 # error code on overflow in the list.
clist = [0 for i in range(N)]
front = ILLEGALINDEX
global rear
rear = 0
def lPush(data):
    global clist
    global front
    global rear
    # appends 'data' to the end of the list if space is available.
    # otherwise returns error.
    if(front == ILLEGALINDEX ):  # list empty.
        front = FIRSTINDEX
        rear = FIRSTINDEX
    elif((rear + 1) % N == front):  # list overflow
        return EINDEXOUTOFBOUND
    else:  # normal case.
        rear = (rear + 1) % N
        clist[rear] = data
        return SUCCESS

def lPrint():
    # prints elements in the list from front to rear.
    nelem = lGetNElements()
    for i in range(nelem):
        print(clist[(front + i) % N]),
    print("\n")

def lGetNElements():
    # returns no of elements in the list.
    if(front == ILLEGALINDEX):
        return 0
    elif(front <= rear):  # no wrapping of rear
        return (rear - front + 1)
    else:
        return(N - front + rear + 1)

def lDeleteK(k):
    # deletes k'th element in the list if present.
    # otherwise returns error.
    # k starts from 1
    # this procedure may be improved by checking for number of elements
    # to be shifted after deleting k'th element. thus we can shift either
    # k+1..N elements or 1..K-1 elements
    global clist
    global front
    global rear
    nelem = lGetNElements()
    print("deleting " + str(k) + "'th element")
    if(k > nelem or k < 1):
        return EINDEXOUTOFBOUND
    index = (front+k-1)%N
    for i in range(k + 1, nelem+1):
        clist[ (front+i - 2)%N ] = clist[ (front+i - 1)%N ]
    if(nelem == 1): # list is empty
        front = ILLEGALINDEX
    elif(k == 1 ):
        front = (front+1)%N
    else:
        rear = (rear - 1+N)%N
    return SUCCESS

def lInsertAfterK(data, k):
    # inserts 'data' after k'th element in the list.
    # if list is full or k is out of bounds, error is returned.
    # k starts from 0.
    global front
    global rear
    nelem = lGetNElements()
    print("inserting " + str(data) + " after the " + str(k) + " 'th element")
    if(k > nelem or k < 0 or nelem == N):
        return EINDEXOUTOFBOUND
    if(nelem == 0):  # list empty
        front = rear = FIRSTINDEX
    else:
        rear = (rear+1)%N
    index = (front+k)%N
    for i in range(nelem, k, -1):
        clist[ (front+i)%N ] = clist[ (front+i - 1)%N ]
    clist[ (front+k)%N ] = data

def main():
    lInsertAfterK(100,0);
    lPrint()
    lPush(0)
    lPush(4)
    lPush(7)
    lPush(1)
    lPush(13)
    lPush(2)
    lPush(5)
    lPrint()
    lInsertAfterK(2,1)
    lPrint()
    lDeleteK(4)
    lPrint()
    lPush(6)
    lPush(3)
    lPush(23)
    lPrint()
    lDeleteK(9)
    lPrint()
    lInsertAfterK(20,9)
    lPrint()
    lDeleteK(10)
    lPrint()
    lInsertAfterK(20,0)
    lPrint()

main()




