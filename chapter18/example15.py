# Chapter 18.15
# Binary Search

MAX = 10  # Max Value

def bsearch(List, n, element):  # Binary Search
    l = 0
    flag = 0
    u = n - 1
    while(l <= u):
        m = (l + u) / 2
        if(List[m] == element):
            print("The element whose value is " + str(element)),
            print(" is present at position " + str(m) + " in the list\n")
            flag = 1
            break
        else:
            if(List[m] < element):
                l = m + 1
            else:
                u = m - 1
    if(flag == 0):
        print("The element whose value is " + str(element)),
        print(" is not present in the list\n")


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
    n = MAX  # Default
    List = []  # Initialize List
    print ("Enter the number of elements in the list max=10\n")
    n = int(raw_input())  # Enter the limit
    print(" ")
    readlist(List, n)  # Enter the values in the list
    print("The list before sorting\n")
    printlist(List, n)
    print ("Enter the element to be searched\n")
    element = int(raw_input())  # Enter the limit
    # Final Result
    bsearch(List, n, element)


main()  # Main Function Entry