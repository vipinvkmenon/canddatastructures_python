# Chapter 9.5
# MANIPULATING AN ARRAY USING POINTERS 3

from ctypes import *

def main():
    a = [0 for i in range(5)]
    b,c= [], []
    for i in range(5):
        a[i] = i
    printarr(a)
    print("\n")
    b.append(2)
    b.append(4)
    b.append(6)
    b.append(8)
    b.append(10)
    b.append(12)
   # a = b
   # a = c //error
    printarr(a)

def printarr(a):
    for i in range(5):
        print(a[i])

def printdetail(a):  # to print address
    for i in range(5):
        print("value in array " + str(a[i]) + " and address is " +str(id(a[i])))

def print_usingptr(a):
    b = a
    for i in range(5):
        print("value in array " + str(b[i]))

main()




