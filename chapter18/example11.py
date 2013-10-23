#Chapter 18.11
# QUICK SORT


MAX = 10


def swap(x, y):  # swapping functions
    temp = x
    x = y
    y = temp
    return x, y


def getkeyposition(i, j):  # Key position function
    return ((i + j) / 2)


def qsort(List, m, n):  # Quicksort Function
    if(m < n):
        k = getkeyposition(m, n)
        List[m], List[k] = swap(List[m], List[k])
        key = List[m]
        i = m + 1
        j = n
        while (i <= j):
            while ((i <= n) and (List[i] <= key)):
                i = i + 1
            while((j >= m) and (List[j] > key)):
                j = j - 1
            if(i < j):
                List[i], List[j] = swap(List[i], List[j])
        List[m], List[j] = swap(List[m], List[j])
        qsort(List, m, j - 1)  # Recursive calls
        qsort(List, j + 1, n)


def readlist(List, n):  # read list
    print("Enter the elements\n")
    for j in range(0, n):
        vals = int(raw_input())
        List.append(vals)


def printlist(List, n):  # display list
    for j in range(0, n):
        print str(List[j]) + " ",
    print "\n"


def main():  # Main Fuction
    List = []
    print ("Enter the number of elements in the list max = 10\n")
    n = int(raw_input())  # input limit
    readlist(List, n)
    print("The list before sorting: \n")
    printlist(List, n)
    qsort(List, 0, n - 1)
    print("The list after sorting is:\n")
    printlist(List, n)



main()  # Calling the main Function
