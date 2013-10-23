#Chapter 29.6
#  MAPPING OF N-QUEUES IN AN ARRAY

N=50 # combined size of all queues
NQ=5 # number of queues
ILLEGALINDEX=-1 # illegal index - - for special cases
EINDEXOUTOFBOUND=-1 # error code on overflow in the queue
SUCCESS=0 # success code.

nqueue=[0 for i in range(N)]
front=[0 for i in range(NQ)]
rear = [0 for i in range(NQ)]

def qInit():
    #/*
     #* initialize front[] to contain ILLEGALINDEX.
     #* ILLEGALINDEX specifies empty queue.
     #*/
    global front
    for i in range(NQ):
        front[i]=ILLEGALINDEX

def qAdd(queue, data):
    #/*
     #* adds 'data' at the end of queue.
     #*/
    global front
    global rear
    global nqueue
    if(queue<0 or queue >= NQ):
        return EINDEXOUTOFBOUND
    maxelem = N/NQ
    nelem = qGetNElements(queue )
    if(nelem == 0 ):
        front[queue] = rear[queue] = maxelem*queue
    elif(nelem == maxelem ):
        return EINDEXOUTOFBOUND
    else:
        rear[queue] = (rear[queue]+1)%maxelem + maxelem*queue
    print("inserting at " + str(rear[queue]))
    nqueue[rear[queue]] = data
    return SUCCESS

def qGetNElements(queue):
    #/*
     #* returns no of elements in queue.
     #*/
    global nqueue
    global front
    global rear
    if(front[queue] ==ILLEGALINDEX):
        return 0
    if(front[queue] <= rear[queue] ):
        return (rear[queue]-front[queue]+1)
    start = N/NQ*queue
    end   = N/NQ*(queue+1)
    return ((end-front[queue]) + (rear[queue]-start+1))

def qDelete(queue):
     #/*
     #* removes front element of queue.
     #*/
    global front
    nelem=qGetNElements(queue)
    print("deleting from queue " + str(queue))
    if(nelem==0):
        return EINDEXOUTOFBOUND
    elif(nelem==1):
        front[queue] = ILLEGALINDEX
    else:
        front[queue] = (front[queue]+1)%(N/NQ) + N/NQ*queue
    return SUCCESS,front

def qIsFull(queue):
     #/*
     #* returns 1 if queue is full, otherwise 0.
     #*/
    return (qGetNElements(queue) == N/NQ )

def qPrint(queue):
     #/*
     #* prints the queue.
     #*/
    global nqueue
    global front
    global rear
    nelem =qGetNElements(queue)
    maxelem = N/NQ
    start =  maxelem*queue
    for i in range(nelem):
        print(nqueue[(front[queue]+i)%maxelem+start]),
    print("\n")

def main():
    qInit()
    print("nelem of 3 is " +str(qGetNElements(3)))
    qAdd(3,0)
    qPrint(3)
    qDelete(3)
    qPrint(3)
    print("nelem of 3 is " +str(qGetNElements(3)))
    qAdd(3,1)
    qAdd(3,2)
    qAdd(3,3)
    qPrint(3)
    qDelete(3)
    qPrint(3)
    qAdd(3,4)
    qAdd(3,5)
    qAdd(3,6)
    qAdd(3,7)
    qAdd(3,8)
    qPrint(3)
    qDelete(3)
    qPrint(3)
    qAdd(3,9)
    qPrint(3)




main()











