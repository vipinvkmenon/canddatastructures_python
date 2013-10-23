#Chapter 18.7
# TRANSPOSE OF A MATRIX

ROW = 3 # Variables
COL = 3 # Variables


def main():  # Main Function
    # Variable Declaration
    a = [[0 for x in xrange(ROW)] for x in xrange(COL)]  # initialise matrix
    read(a, ROW, COL)
    print("The matrix is\n")
    dis(a, ROW, COL)
    trans(a, ROW, COL)  # Transpose function
    print("The transpose of the matrix is\n")
    # Final Result
    dis(a, ROW, COL)


def read(c, i, k):  # Read Matrix
    j, l = 0, 0
    print("Enter the array")
    for j in range(0, i):
        for l in range(0, k):
            temp = int(raw_input())
            c[j][l] = temp

def dis(d, i, k):  #Display Matrix
    j, l = 0, 0
    for j in range(0, i):
        for l in range(0, k):
            print(str(d[j][l]) + " "),
        print("\n")


def trans(mat, k, l):  # Transpose of Matrix
    i, j, temp = 0, 0, 0
    for i in range(0, k):
        for j in range(i + 1, l):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp

main()  # Main Function Entry