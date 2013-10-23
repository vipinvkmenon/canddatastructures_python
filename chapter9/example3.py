# Chapter 9.3
# ACCESSING AN ARRAY USING POINTERS

def main():  # Main function
    a = []
    for i in range(5):
        a.append(i)
    printdetail(a)  # Print array and address
   #  print_usingptr(a) 

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



main()
