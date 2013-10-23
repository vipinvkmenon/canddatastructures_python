# Chapter 9.4
# ACCESSING AN ARRAY USING POINTERS

def main():  # Main function
    a = []
    for i in range(5):
        a.append(i)
    print_usingptr(a)
    

def printarr(a): # To print array
    for i in range(5):
        print("value in array " + str(a[i]))

def printdetail(a):  # to print address
    for i in range(5):
        print("value in array " + str(a[i]) + " and address is " +str(id(a[i])))

def print_usingptr(a):
    b = a
    for i in range(5):
        print("value in array " + str(b[i]))



main()  # Main function entry
