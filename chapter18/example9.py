#Chapter 18.9
# FINDING THE SADDLE POINT OF A MATRIX

from ctypes import *  # Additional import for pointers

ROW = 3
COL = 3


def main():  # Main Function
    # Varialbes Declarations
    a = [[0 for x in xrange(ROW)] for x in xrange(COL)]  # initialise matrix
    m, n = pointer(c_int(0)), pointer(c_int(0))  # pointers m and n

    read(a, ROW, COL)
    print("The matrix is\n")
    dis(a, ROW, COL)
    i = sadd_pt(a, 3, 3, m, n)
    print("The saddle point is " + str(i) + " & its position is row : "),
    # Final Result
    print(str(m[0] + 1) + " col : " + str(n[0] + 1) + "\n")


def read(c, i, k):  # REad Matrix
    j, l = 0, 0
    print("Enter the array")
    for j in range(0, i):
        for l in range(0, k):
            temp = int(raw_input())
            c[j][l] = temp


def dis(d, i, k):  # Display Matrix
    j, l = 0, 0
    for j in range(0, i):
        for l in range(0, k):
            print(str(d[j][l]) + " "),
        print("\n")


def sadd_pt(mat, k, l, row, col):  # Function to find Saddle Point
    #Variables Declaration
    Min = 32767
    i, j, m, n, p = 0, 0, 0, 0, 0
    while(i < k):
        Min = 32767
        m = i
        p = 0
        for j in range(0, l):
            if(mat[i][j] < Min):
                Min = mat[i][j]
                n = j
        for j in range(0, k):
            if(Min >= mat[j][n]):
                p = p + 1
        if (p == 3):
            row[0] = m
            col[0] = n
            return Min
        i = i + 1
    print("No Saddle point exists\n")


main()  # Main Function entry