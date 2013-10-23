#Chapter 18.10
# BUBBLE SORT



MAX = 10


def swap(x, y):  # swapping functions
    temp = x
    x = y
    y = temp
    return x, y


def bsort(List, n):  # bubbble sort
    for i in range(0, n - 1):
        for j in range(0, n - (i + 1)):
            if (List[j] > List[j + 1]):
                List[j], List[j + 1] = swap(List[j], List[j + 1])



def readlist(List, n):
    for j in range(0, n):
        vals = int(raw_input())
        List.append(vals)


def printlist(List, n):
    print(" The list is:\n")
    for j in range(0, n):
        print str(List[j]) + " ",
    print "\n"

def main():  # Main Function
    List = []
    print ("Enter the number of elements in the list max = 10\n")
    n = int(raw_input())  # input limit
    readlist(List, n)
    print("The list before sorting: \n")
    printlist(List, n)
    bsort(List, n)
    print("The list after sorting:\n")
    printlist(List, n)

main()  # Main Function




