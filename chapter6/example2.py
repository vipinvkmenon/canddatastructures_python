# Chapter 6.1
# POinters

from ctypes import *
def main():  #  Main function
    i = 10
    i = py_object(i)
    ia = i
    # k = i + j
    print("The address of i is " + str(id(ia)))
    print("The value at the location is " + str(i.value))
    print("The value at the location is " + str(ia.value))
    ia.value= 50
    print("The value at the location is " + str(i.value))

main()  # Main Function entry
