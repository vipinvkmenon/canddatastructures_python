# Chapter 9.8
# Pointer Arrays

from ctypes import *
a = [0 for x in range(5)]

def main():
    i1, i2, i3, i4, i5 = 4, 3, 2, 1, 0
    a[0] = pointer(c_int(i1))  # passing reference of i1 to a[0]
    a[1] = pointer(c_int(i2))
    a[2] = pointer(c_int(i3))
    a[3] = pointer(c_int(i4))
    a[4] = pointer(c_int(i5))

    printarr(a)
    printarr_usingptr(a)

def printarr(a):
    print("Address\t     Address in array\tvalue")
    for j in range(5):
        print(str(id(a[j])) + "\t" + str(id(a[j][0])) +  "\t" + str(a[j][0]))

def printarr_usingptr(a):
    print("Using Pointer")
    for j in range(5):
        print(" Value of elements " +str(a[j][0]) + "  " + str(id(a[j][0])) +  "  " + str(id(a[j])))  # Value.  address in array,  address of array
    
    
main()  # Main Function Entry
