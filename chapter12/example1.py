#Chapter 12.1
# Dynamic Memory Allocation

from ctypes import *
def main():
    i , cnt, Sum = 0, 0, 0
    base = []
    print("How many integersyou have to stores\n")
    cnt = int(raw_input())  # Input limit
    print("the base of allocation is " + str(id(base)))
    if (base == None):
        print("Unable to allocate size")
    else:
        for j in range(cnt):
            base.append(5)  #Add vals ito array
    Sum = 0
    for j in range(cnt):
        Sum = Sum + base[j]  # find sum
    print("total sum is " + str(Sum))
    base = 0  # dereference
    print("the base of allocation is " + str(id(base)))  # memory locations
    base = []
    print("the base of allocation is " + str(id(base)))
    base = []
    print("the base of allocation is " + str(id(base)))
    base = []
    print("the base of allocation is " + str(id(base)))
      
    
    

main()


    
    
    
