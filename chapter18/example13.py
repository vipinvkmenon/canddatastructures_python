# Chapter 18.13
# HEAPSORT

MAX = 10  # Max Value


def swap(x,y):  # Swap Function
    temp = x
    x = y
    y = temp
    return x, y

def adjust(List, i, n):  # Adjust  Ith element to satisfy Heap property
    k = List[i]
    flag = 1
    j = 2 * i
    while(j <= n and flag == 1):
        if(j < n and List[j] < List[j + 1]):
            j = j + 1
        if (k >= List[j]):
            flag = 0
        else:
            List[j / 2] = List[j]
            j = j * 2
    List[j / 2] = k


def build_initial_heap(List, n):  # Initial Heap Builder
    for i in range(n / 2, -1, -1):
        adjust(List, i, n - 1)


def heapsort(List, n):  # Heapsort function
    build_initial_heap(List, n)  # Build initial heap
    for i in range(n - 2, -1, -1):
        List[0], List[i + 1] = swap(List[0], List[i + 1])  # Swap
        adjust(List, 0, i)  # Adjust


def readlist(List, n):  # Read List
    for i in range(0, n):
        vals = int(raw_input())
        List.append(vals)


def printlist(List, n):  # Print List
    for i in range(0, n):
        print(str(List[i]) + " "),
    print("\n")


def main(): # Main Function
# Variables
    List = []  # Initialize List
    print ("Enter the number of elements in the list max=10\n")
    n = int(raw_input())  # Enter the limit
    print(" ")
    readlist(List, n)  # Enter the values in the list
    print("The list before sorting\n")
    printlist(List, n)
    heapsort(List, n)  # Call heapsort
    # Final Output
    print("The list after sorting\n")
    printlist(List, n)


main()  # Main Function Entry