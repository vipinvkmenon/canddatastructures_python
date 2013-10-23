# Chapter 9.6
# Two Dimension Array

def main():
    a = [[0 for x in xrange(2)] for x in xrange(3)]  # initialise matrix 3x2
    for i in range(3):
        for j in range(2):
            a[i][j] = i
    printdetail(a)
   
def printarr(a):
    for i in range(3):
        for j in range(2):
            print("value in array " + str(a[i][j]))

def printdetail(a):
    for i in range(3):
        for j in range(2):
            print("value in array " + str(a[i][j]) + " and address is "),
            print(str(id(a[i][j])))

def print_usingptr(a):
    b = a
    for i in range(3):
        for j in range(2):
            print("value in array " + str(b[i][j]) + " and address is "),
            print(id(b[i][j]))



main()  # Entry to main function

    
    
    

 
