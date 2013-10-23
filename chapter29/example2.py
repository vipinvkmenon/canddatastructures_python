#Chapter 29.2
#  THE N-COINS PROBLEM


MINGROUPSIZE = 10
EPSILON = 0.08


def adjustPartition(a, n,p,m,i):
    #/*
     #* slide the partition boundary from i  forward or backward to get
     #* better partition and return the index of the last element in the
     #* partition.
     #* i  >=  1.
     #*/
    aindex =  i*MINGROUPSIZE
    startj =  aindex-MINGROUPSIZE/4
    finalj = aindex+MINGROUPSIZE/4
    k=(i  - 1)*MINGROUPSIZE
    ones = 0
    nelem=0
    while(k<startj):
        ones +=  a[k]
        k = k +1
        nelem = nelem+1
    # the bias of the coin uptil  now here is ones/nelem
    j=startj
    while(j<finalj):
        ones +=  a[j]
        nelem = nelem+1
        if(abs(ones/nelem-p[i]) >=EPSILON):
            break
        j = j+1
    return j

def findChange(a,n,p,m):
    #/*
    #* the running probabilities are given in p[m].
    #* find the points of coin change from them.
    #*/
    for i in range(1,m):
        if(abs(p[i]-p[i-1]) >= EPSILON):
            return adjustPartition(a, n, p, m, i)
    return -1

def findProb(a,n,p):
    #/*
    #* find the average probabilities of groups in a[n]  and store in p.
    #*/
    j=-1
    nelem = 0
    for i in range(n):
        if(i%MINGROUPSIZE  == 0):
            ones = 0
            nelem = 0
            j = j+1
        if(a[i] ==1):
            ones =ones+1
            p[j]=ones/(nelem+1)
        else:
            p[j]=ones/(nelem+1)
        nelem = nelem+1
    return j+1,p

def printAverage(a, partindex):
    #/*
     #* print average of this new partition a[O.  .partindex-1;
     #*/
    ones = 0
    for i in range(partindex):
        ones += a[i]
        ones = ones + 1.00
    print("average  = " +str(ones/partindex))

def findPartition(a, n, p, startoff):
    m,p = findProb(a,n,p)
    print p
    partindex=findChange(a,n,p,m)
    if(partindex != -1):
        print("partiti0n  at " +str(startoff+partindex))
        printAverage(a,  partindex)
        findPartition(a,  n -partindex, p, startoff+partindex)
    else:
        printAverage(a,n)

def main():
    a = [0,0,0,  1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0, 0,0,1,0,0,1,0,0,0,1,0]
    #a = [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0, 0,0,1,0,0,1,0,0,0,1,1]
    n=len(a)
    p = [0 for i in range((n+MINGROUPSIZE - 1)/MINGROUPSIZE)]
    findPartition(a,n,p,0)

main()









