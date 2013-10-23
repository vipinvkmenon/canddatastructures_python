#Chapter 29.1
#  THE TWO-CLASS CLASSIFICATION PROBLEM


FALSE = 0
TRUE = 1
tp = 0


def computerD(x,n,w):
    #/*
    #* compute the value of the discriminant function D using the xis and wis.
    #* D =  w0 +  w1x1 +  w2x2 +  ... + wnxn.
    #*/
    d = w[0]
    for i in range(1, n+1):
        d += int(w[i])* int(x[i])
    return d

def signum(d):
     #/*
    #* signum(d)  =  1 if d>=O
    #*            =  -1 otherwise.
    #*/
    if(d >= 0):
        return 1
    return -1

def updateW(x, n, w, c, k, d):
       #/*
    #* update the ws as the discriminant function was different than the class
    #* value.
    #* wi +=  cdxi for l<=i<=n.
    #* w0 +=  cdk.
    #*/
    global tp
    print tp
    tp +=c*d*k
    w[0] =tp
    for i in range(1,n+1):
        w[i] = c*d*k*int(x[i])
    return w

def printHeader(n):
    #/*
    #* print header of the output
    #*/
    for i in range(1,n+1):
        print(i),
    print("d\t")
    for i in range(0,n+1):
        print("old w " + str(i) +"\t"),
    print("D\tError?\t"),
    for i in range(i,n+1):
        print("new w " +str(i) + "\t")
    print("\n")

def findk(fp, n):
    k = 0
    count = 0
    fp.close
    fp = open("adb.dat",'r')
    tempk = fp.readlines()
    print(tempk)
    for i in range(1,len(tempk)):
        k += int(tempk[i])
    for i in range(((len(tempk)-1)%n)+1):
        count = count + 1
    k /= count*n
    k = abs(k)
    return k

def printArray(xrow, n,g):
    #/*
    #* print xorw[0.  .n-1].
    #*/
    for i in range(g,n):
        print(xrow[i]),
        print("\t"),

def main():
    c = 1
    g = 2
    h = 0
    wChanged = TRUE
    fp = open("adb.dat",'w')
    fp.write("5\n")
    fp.write("-1\n")
    fp.write("-10\n")
    fp.write("22\n")
    fp.write("-35\n")
    fp.write("40\n")
    fp.close()
    fp = open("adb.dat",'r')
    lns = fp.readlines()
    n = int(lns[0])
    x = [0 for i in range(n+1)]
    w = [0 for i in range(n+1)]
    k = findk(fp,n)
    print(k)
    while(wChanged == TRUE):
        wChanged = FALSE
        x= lns
        for i in range(1,len(lns)):
            g = g+1
            printArray(x,n,g)
            printArray(w,n+1,h)
            D = computerD(x,n,w)
            if(signum(D) != int(x[1])):
                wChanged = TRUE
                w = updateW(x, n, w, int(c), int(k), int(x[1]))
                print("yes\t"),
            else:
                print("no\t"),
                printArray(w,n+1,h)
                print("\n")



main()







