
#Chapter 23.5
# IMPLEMENT K-WAY SORT-MERGE TO SORT A FILE CONTAINING RECORDS

N = 80
K = 2
DATAFILE = "main.txt"
TEMPFILE = "temp.txt"
FALSE = 0
TRUE = 1
lineslist = []

class node:

    def __init__(self,vl, st):
        self.val = vl
        self.s = st

buf = [node(0,"") for i in range(K)]  # buffer used for merging.
rec = [0 for i in range(K)] # record numbers of nodes in buffer.

def getNRecords(filename):
    # returns no of records in file filename using size of the file.
    fp = open(filename, 'r')
    fp.seek(0,0)
    off = fp.readline().split("  ")
    fp.close()
    return(len(off)-1)

def writeToFile(filename, n):
    # writes record n to file filename.
    fp = open(filename, 'a')
    fp.write(str(n.val) + "." + n.s+"  ")
    fp.close()

def readFromFile(filename, n, off):
    # reads a record at offset off from file filename into n.
    # off is number of records before the record in the file (NOT bytes).
    # off starts from 0.
    #global lineslist
    lineslist = []
    if(off >= getNRecords(filename)):
        print("ERROR: reading beyond the file.\n")
        return lineslist
    print("total records are " +str(getNRecords(filename)))
    fp = open(filename, 'r')
    fp.seek(0,0)
    lines =fp.readline().split("  ")
    #print("the line is" + str(lines))
    fp.close()
    for j in range(len(lines)-1):
        lineslist.append(lines[j].split("."))
    print("the len of liselist is " +str(len(lineslist)))
    return lineslist

def writeFun(filename):
    # writes some data to filename.
    data = [node(5,"five"), node(3,"three"), node(4,"four"), node(8,"eight"),
    node(7,"seven"),node(6,"six"), node(9,"nine"),
    node(10,"ten"),node(1,"one"), node(2,"two")]
    for i in range(10):
        writeToFile(filename, data[i])

def readFun(filename):
    # reads filename and prints the data.
    n = None
    nrec =  getNRecords(filename)
    for i in range(nrec):
        n = readFromFile(filename, n, i)
        print(str(i) + " = {" + str(n[i][0]) + ", " + str(n[i][1]) + "}")

def copyrec(rec, rec2):
    rec2 = rec
    for i in range(K):
        rec2[i] =rec[i]
    return rec, rec2

def fillbuf(start, l, nrec, srcfile):
    # fills buf and rec with appropriate values.
    # l is length of each run.
    # start is rec no of first rec in first run.
    # data is in srcfile in nrec records.
    global rec
    global buf
    print("start = " + str(start) + "l = " + str(l))
    for i in range(K):
        startoff = start + l* i
        if(startoff >= nrec):
            break
        rec[i] = startoff
        print("buf[" + str(i) + "] = " + str(startoff))
        readFromFile( srcfile, buf, startoff )
    for j in range(i,K):
        rec[j] = -1
    #d = raw_input()

def updatebuf(buf, rec, rec2, prevrec, l, srcfile, nrec):
    # updates buf+rec2 as rec2[prevrec] was output.
    # read appropriate record from srcfile if necessary.
    # rec still contains the original rec nos which can be used for
    # checking ends of runs.
    # l is runlength.
    if ((rec2[prevrec] < (nrec - 1)) and (rec2[prevrec] < (rec[prevrec] + l - 1))):
        # rec2[prevrec] was NOT the last rec of that run.
        rec2[prevrec] = rec2[prevrec] + 1
        readFromFile( srcfile, buf[prevrec], rec2[prevrec])
    else:
        # rec2[prevrec] was the last rec of that run.
        rec2[prevrec] = -1 # job of this run is over.

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

def merge(srcfile, dstfile, buf, rec2, l, nrec):
    # rec2 contains record numbers being compared; global rec also contains
    # the same at this point.
    # buf contains their actual data.
    # l is runlength.
    # srcfile is needed for reading next data.
    # the data is appended to dstfile.
    # total no of records being written is min(l*k,nrec-rec[0]).
    totalrec = l * K
    nrecremaining = nrec - rec[0]
    if( nrecremaining < totalrec ):
        totalrec = nrecremaining
    print("totalrec = " + str(totalrec) + "nrecremaining= " +str(nrecremaining))
    for i in range(totalrec):
        nextrec = getMin( buf, rec2 ) # here goes the comparison.
        print("after getMin: min = " +str(nextrec) + " rec2= " + str(rec2[0])),
        print(str(rec2[1])),
        #print(str(rec2[2])),
        print(str(buf[0].val)),
        print(str(buf[1].val)),
        #print(str(buf[2].val))
        if(nextrec == -1):
            print("ERROR: merge(): all rec2 are -1!\n")
            return 0
    # printf( "min=%d.\n", nextrec );
    # this is the index in rec2 of next record to be output.
    writeToFile( dstfile, buf[nextrec] )
    # remove this written record. read new record from srcfile if needed.
    updatebuf( buf, rec, rec2, nextrec, l, srcfile, nrec )
    # printf( "after updatebuf : rec2=%d %d %d.\n", rec2[0], rec2[1], rec2[2] )

def mergedriver(srcfile, dstfile):
    # sort+merge srcfile and store in dstfile.
    nrec = getNRecords(srcfile)
    l = 1
    rec2 = [0 for i in range(K)]
    global rec
    while(l < nrec):
        #l is length of each run.
        #no of runs = ceil( nrec/l );
        # we need to consider only K runs at a time.
        i = 0
        while(i < nrec):
            # fill buf with appropriate values.
            fillbuf( i, l, nrec, srcfile )
            rec, rec2 = copyrec( rec, rec2 )
            merge( srcfile, dstfile, buf, rec2, l, nrec )
            i += l*K
        l *= K
        tempname = srcfile
        srcfile = dstfile
        dstfile = tempname
        fp=open(dstfile,'w+')
        fp.close()
    # sorted file is srcfile.
    print("\n\n\n")
    readFun(srcfile)

def main():
    srcfile = DATAFILE
    dstfile = TEMPFILE
    fp=open(DATAFILE,'a')
    fp.close()
    fp=open(DATAFILE,'w')
    fp.close()
    writeFun( srcfile )
    readFun( srcfile )
    print("nrec= " + str(getNRecords(srcfile)))
    mergedriver(srcfile, dstfile)

main()







