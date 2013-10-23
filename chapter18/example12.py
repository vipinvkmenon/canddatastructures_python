#Chapter 18.12
# MERGE SORT

MAX = 10  # Max size


def merge(List, List1, k, m, n):  # Merge Function
    i = k
    j = m + 1
    while(i <= m and j <= n):
        if (List[i] <= List[j]):
            List1[k] = List[i]
            i = i + 1
            k = k + 1
        else:
            List1[k] = List[j]
            j = j + 1
            k = k + 1
    while(i <= m):
        List1[k] = List[i]
        i = i + 1
        k = k + 1
    while(j <= n):
        List1[k] = List[j]
        j = j + 1
        k = k + 1


def mpass(List, List1, l, n):  # merge the adjacent sorted lists
    i = 0
    while(i <= (n - 2 * l + 1)):
        merge(List, List1, i, (i + l - 1), (i + 2 * l - 1))
        i = i + 2 * l
    if ((i + l - 1) < n):
        merge(List, List1, i, (i + l - 1), n)
    else:
        while(i <= n):
            List1[i] = List[i]
            i = i + 1


def msort(List, n):  # MergeSort Function
    l = 1
    List1 = [0 for x in range(MAX)]  # Initialzie List filled with 0
    while (l <= n):
        mpass(List, List1, l, n)
        l = l * 2
        mpass(List1, List, l, n)
        l = l * 2

def readlist(List, n):  # Read List
    for i in range(0, n):
        vals = int(raw_input())
        List.append(vals)


def printlist(List, n):  # Print List
    for i in range(0, n):
        print(str(List[i]) + " "),
    print("\n")

def main():  # Main function
    List = []
    print ("Enter the number of elements in the list max=10\n")
    n = int(raw_input()) #Enter the limit
    print(" ")
    readlist(List, n)
    print("The list before sorting\n")
    printlist(List, n)
    msort(List, n - 1)
    print("The list after sorting\n")
    printlist(List, n)


main()  # Entry
