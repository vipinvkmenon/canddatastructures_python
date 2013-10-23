
#Chapter 23.5
# IMPLEMENT K-WAY SORT-MERGE TO SORT A FILE CONTAINING RECORDS

N = 80
K =8
DATAFILE = "main.txt"
TEMPFILE = "temp.txt"
FALSE = 0
TRUE = 1


class node:

    def __init__(self,vl, st):
        self.val = vl
        self.s = [" " for i in range(N)]
        for i in range(len(st)):
            self.s[i] = st[i]



buf = [node(0,"") for i in range(K)]  # buffer used for merging.
rec = [0 for i in range(K)] # record numbers of nodes in buffer.

def getNRecords(filename):
    # returns no of records in file filename using size of the file.
    fp = open(filename, 'r')
    #fp.seek(0,0)
    off = fp.readlines()
    fp.close()
    return(len(off))

def writeToFile(filename, n):
    fp = open(filename,'a')
    g = ["" for i in range(N)] # 80 size array
    cnt = 0
    for i in str(n.val):
        g[cnt]=i
        cnt = cnt+1
    g[cnt] = "."
    cnt = cnt+1
    i=0
    while(cnt<N):
        g[cnt]=n.s[i]
        i = i +1
        cnt = cnt+1
    fp.write("".join(g)+ "\n") # string formatted to 80 chars
    #print "position",
    #print fp.tell()
    fp.close()

def readFromFile(filename, n, off):
    #/*
     #* reads a record at offset off from file filename into n.
     #* off is number of records before the record in the file (NOT bytes).
     #* off starts from 0.
     #*/
    print("reading rec no " + str(off))
    if(off >= getNRecords(filename)):
        print("ERROR: reading beyond the file.\n")
        return None
    print("total records are " + str(getNRecords(filename)))
    fp = open(filename,'r')
    fp.seek(off*81,1) # seek off positions from current position
    k = fp.readline().split(".")
    n.val = int(k[0])
    g = k[1]
    for i in range(len(g)):
        n.s[i]= g[i]
    return n

def writeFun(filename):
    # writes some data to filename.
    data = [node(4,"four"), node(3,"three"),node(5,"five"), node(8,"eight"),
    node(7,"seven"),node(6,"six"), node(9,"nine"),
    node(10,"ten"),node(1,"one"), node(2,"two")]
    for i in range(len(data)):
        writeToFile(filename, data[i])

def readFun(filename):
    #/*
     #* reads filename and prints the data.
     #*/
    n = node(0,"")
    nrec = getNRecords(filename)
    for i in range(nrec):
        n = readFromFile(filename,n,i)
        print(str(i) +"="),
        print(str(n.val)+", " + "".join(n.s))

def copyrec(rec, rec2):
    rec2 = rec
    #for i in range(0,K):
        #rec2[i]=rec[i]
    return rec2

def fillbuf(start,l,nrec,srcfile):
    #/*
     #* fills buf and rec with appropriate values.
     #* l is length of each run.
     #* start is rec no of first rec in first run.
     #* data is in srcfile in nrec records.
     #*/
    global buf
    global rec
    print("start = " +str(start)+" l = "+str(l))
    i = 0
    while(i<K):
        startoff=start+l*i
        if(startoff >= nrec):
            break
        rec[i]=startoff
        print("buf[" + str(i) + "]= " +str(startoff))
        buf[i]=readFromFile(srcfile,buf[i],startoff)
        i = i+1
    while(i<K):
        rec[i]=-1
        i = i+1
    #frg=raw_input()

def updatebuf(buf,rec,rec2,prevrec,l,srcfile,nrec):
     #/*
      #* updates buf+rec2 as rec2[prevrec] was output.
      #* read appropriate record from srcfile if necessary.
      #* rec still contains the original rec nos which can be used for
      #* checking ends of runs.
      #* l is runlength.
      #*/
    if(rec2[prevrec]<nrec-1 and rec2[prevrec]<rec[prevrec]+l-1):
        rec2[prevrec]=rec2[prevrec]+1
        buf[prevrec] = readFromFile(srcfile,buf[prevrec],rec2[prevrec])
    else:
        print("")
        rec2[prevrec] = -1
    return buf, rec2

def getMin(buf, rec2):
    # returns index in buf of that record which has min sorting value.
    # rec2 is needed for checking whether a buf entry is valid.
    minval = 9999
    minindex = -1
    for i in range(K):
        if(rec2[i] != -1 and buf[i].val < minval):
            minval = buf[i].val
            minindex = i
    return minindex

def merge(srcfile,dstfile,buf,rec2,l,nrec):
     #/*
    #* rec2 contains record numbers being compared; global rec also contains
    #* the same at this point.
    #* buf contains their actual data.
    #* l is runlength.
    #* srcfile is needed for reading next data.
    #* the data is appended to dstfile.
    #* total no of records being written is min(l*k,nrec-rec[0]).
    #*/
    global rec
    totalrec=l*K
    nrecremaining = nrec-rec[0]
    if(nrecremaining < totalrec):
        totalrec = nrecremaining
    print("totalrec= " +str(totalrec) + " nrecremaining= "+ str(nrecremaining) +"\n")
    for i in range(totalrec):
        nextrec=getMin(buf,rec2)
        print("after getMin: min = " +str(nextrec) + " rec2= " + str(rec2[0])),
        print(str(rec2[1])),
        print(" buf = "),
        print(str(buf[0].val)),
        print(str(buf[1].val))
        print("\n")
        if(nextrec == -1):
            return buf, rec2
        writeToFile(dstfile,buf[nextrec])
        buf, rec2 = updatebuf(buf, rec, rec2, nextrec, l, srcfile, nrec)
    return buf, rec2

def mergedriver(srcfile,dstfile):
    global rec
    global buf
    nrec = getNRecords(srcfile)
    rec2 = [0 for i in  range(K)]
    #tempname = ["" for i in range(N)]
    l = 1
    while(l<nrec):
        i = 0
        while(i<nrec):
            fillbuf(i,l,nrec,srcfile)
            rec2 = copyrec(rec,rec2)
            buf, rec2 = merge( srcfile, dstfile, buf, rec2, l, nrec)
            i+= l*K
        tempname = srcfile
        srcfile = dstfile
        dstfile=tempname
        fp = open(dstfile,'w+')
        fp.close()
        l*=K
    readFun(srcfile)




def main():
    #global buf
    srcfile = DATAFILE
    dstfile = TEMPFILE
    fp = open(srcfile,'w+')
    fp.close()
    fp=open(dstfile,'w+')
    fp.close()

    #print getNRecords(DATAFILE)
    #for i in range(K):
        #buf[i]= readFromFile(DATAFILE,buf[i],i)
        #print buf[i].s
    writeFun(srcfile)
    readFun(srcfile)
    print("nrec="),
    print getNRecords(srcfile)
    mergedriver(srcfile,dstfile)
main()









