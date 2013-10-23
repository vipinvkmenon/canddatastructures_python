#Chapter 23.2
#  PROGRAM TO FIND THE SADDLE POINT OF A MATRIX

M = 3
N = 3

def findMin(a, row):
    # find min value in row of a.
    # return the value.
    Min = a[row][0]
    for j in range(1,N):
        if( a[row][j] < Min ):
            Min = a[row][j]
    return Min

def findMax(a, col):
    # find max val in col of a.
    # return the value.
    Max = a[0][col]
    for i in range(1, M):
        if( a[i][col] > Max ):
            Max = a[i][col]
    return Max


def saddle(a):
    # finds ALL saddle points of a if exist.
    for i in range(M):
        Min = findMin(a, i)
        for j in range(N):
            Max = findMax(a, j)
            if(Min == Max):
                print("Saddle : ( " +str(i) + ", " + str(j) + " )")
    

def main():
    a = [[5, 7, 3], [7, 7, 9], [7, 1, 2]]
    saddle(a)
    
main()
