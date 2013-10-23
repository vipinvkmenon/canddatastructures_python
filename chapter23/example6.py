#Chapter 23.6
# PLATEAU IN A MATRIX

COLS = 5
MININT = -99999

def Filter(a, i, j, k, l, rows, cols):
    # filter the matrix of size k*l starting from a[i][j].
    # size of the matrix is rows*cols.
    # k, l start with 1.
    Sum = 0
    if(i+k > rows or j + l > cols): # the matrix was already considered with smaller k, l.
        return MININT
    iii = 0
    while(iii < k and (i + iii < rows)):
        jjj = 0
        while(jjj < l and (j+ jjj < cols)):
            Sum += a[i+iii][j+jjj]
            if(Sum< 0):
                return Sum  # this is reqd: if all vals -ve.
            jjj = jjj + 1
        iii = iii + 1
    return Sum

def printMatrix(a,i, j, k, l, rows, cols):
    # print a rectangular region of a from a[i][j] of size k*l if possible.
    # the matrix is bounded by rows*cols.
    iii = 0
    while(iii < k and (i + iii < rows)):
        jjj = 0
        while(jjj < l and (j+ jjj < cols)):
            print(a[i+iii][j+jjj]),
            jjj = jjj + 1
        print("\n")
        iii = iii + 1
    d= raw_input()

def plateau(a, rows, cols):
    # finds a rectangular region having max sum of elements in it.
    maxsum = a[0][0]
    maxrow1=0
    maxrow2=0
    maxcol1=0
    maxcol2=0
    for i in range(rows):
        for j in range(cols):
            # generate k*l matrix using a[i][j].
            for k in range(1, rows+1):
                for l in range(1, cols +1):
                    Sum=Filter(a, i, j, k, l, rows, cols)
                    if(Sum > maxsum):
                        maxsum=Sum
                        maxrow1 = i
                        maxcol1 = j
                        maxrow2 = i + k - 1
                        maxcol2 = j + l - 1
    print("Sum = " + str(Filter(a, maxrow1, maxcol1, maxrow2-maxrow1+1, maxcol2-maxcol1+1, rows, cols)))
    printMatrix(a, maxrow1, maxcol1, maxrow2-maxrow1+1, maxcol2-maxcol1+1, rows, cols)

def main():
    a = [[5,-1,-2,-4,1], [-3,2,10,-6,3], [-1,9,-11,-7,9], [3,101,3,-2,-96], [-1,-2,0,3,-3], [-1,-2,-3,2,-3]]
    #
    plateau(a, len(a), COLS)



main()
