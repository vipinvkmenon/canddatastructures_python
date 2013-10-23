#Chapter 18.8
# TRANSPOSE OF A MATRIX
ROW = 3
COL = 3


def main():
    # Variables Declarations
    a = [[0 for x in xrange(ROW)] for x in xrange(COL)]  # initialise matrix
    b = [[0 for x in xrange(ROW)] for x in xrange(COL)]  # initialise matrix
    read(a, ROW, COL)
    print("The matrix is\n")
    dis(a, ROW, COL)
    trans(a, b, ROW, COL)  # Transpose function
    print("The transpose of the matrix is\n")
    # Final Result
    dis(b, ROW, COL)


def read(c, i, k):  # Read Matrix
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

def trans(mat, tr_mat, k, l):
    i, j = 0, 0
    for i in range(0, k):
        for j in range(0, l):
            tr_mat[i][j] = mat[j][i]


main()