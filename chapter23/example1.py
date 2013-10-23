# Chapter 23.1
# CALCULATE THE VALUE OF AN N × N DETERMINANT

N = 3
EPSILON = 1e-10
TRUE = 1
FALSE = 0

def Print(a):
    for i in range(N):
        for j in range(N):
            print(a[i][j])
    print("\n")

def divRow(a, row, divisor):
    for j in range(N):
        a[row][j] =(a[row][j]*1.0)/ divisor
    return a


def subRow(a, row1, row2):
    for j in range(N):
        a[row1][j] -= a[row2][j]
    return a
        

def anyZero(a):
    for i in range(N):
        if(abs(a[i][i]) <= EPSILON):
            return TRUE
    return FALSE
def makeUpper(a):
    factor = 1.0
    for i in range(1,N):
        for j in range(i):
            temp = a[i][j]
            print("temp is " + str(temp))
            if(abs(temp) > EPSILON):
                print("factor= " +str(factor) + " dividing row= " + str(i)),
                print("by " +str(temp))
                a = divRow(a, i, temp)
                Print(a)
                factor *= temp
            temp = a[j][j]
            if(abs(temp) > EPSILON and abs(temp - 1) > EPSILON):
                print("factor= " +str(factor) + " dividing row= " + str(j)),
                print("by " +str(temp))
                a = divRow(a, j, temp)
                Print(a)
                factor *= temp
            if(abs(a[i][j]) > EPSILON):
                print("factor= " +str(factor) + " -= " + str(i)),
                print("by " +str(j))
                subRow(a,i, j)
                Print(a)
            if (anyZero(a) == TRUE):
                return 0
    a[N-1][N-1] *= factor
    return 1
def multDia(a):
    # Returns multiplication of diagonal elements
    factor = 1
    for i in range(N):
        factor *= a[i][i]
    return factor

def main():
    a = [[8,0,1],[2,1,3],[5,3,9]]  # initialise matrix
    Print(a)
    
    factor = makeUpper(a)
    print(factor)
   
    print("determinint " + str(factor*multDia(a)))

main()
        
            
    
    
