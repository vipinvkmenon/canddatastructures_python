# Chapter 18.14
# Linear/Sequential Search

MAX = 10  # Max Value


def lsearch(List, n, element):  # Linear Search Function
    flag = 0
    for i in range(0, n):
        if(List[i] == element):
            print("The element whose value is " + str(element)),
            print(" is present at " + str(i))
            flag = 1
            break
    if(flag == 0):
        print("The element whose value is " + str(element)),
        print(" is not present in the list")


def readlist(List, n):  # Read List
    for i in range(0, n):
        vals = int(raw_input())
        List.append(vals)


def printlist(List, n):  # Print List
    for i in range(0, n):
        print(str(List[i]) + " "),
    print("\n")


def main(): # Main Function
# Variables List,element and n

    List = []  # Initialize List
    print ("Enter the number of elements in the list max=10\n")
    n = int(raw_input())  # Enter the limit
    print(" ")
    readlist(List, n)  # Enter the values in the list
    print("The list before sorting\n")
    printlist(List, n)
    print ("Enter the element to be searched\n")
    element = int(raw_input())  # Enter the limit
    # Final Output
    lsearch(List, n, element)


main()  # Main Function Entry