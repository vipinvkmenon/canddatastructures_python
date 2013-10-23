# Chapter 9.2
#ADDRESS OF EACH ELEMENT IN AN ARRAY

def main():  # Main Function
    a = []
    for i in range(5):
        a.append(i)
    printarr(a)  # Prints the array
   # printdetail(a) # Remove hash to printaddress

def printarr(a): # To print array
    for i in range(5):
        print("value in array " + str(a[i]))

def printdetail(a):  # to print address
    for i in range(5):
        print("value in array " + str(a[i]) + " and address is " +str(id(a[i]))) 

main()

    
