#Chapter 18
# MERGING OF TWO SORTED LISTS

a, b, c = [], [], []


def main():
    print("Enter the elements of first list \n")
    read(a, 5)  # Read the list
    print("The elements of first list are \n")
    dis(a, 5)  # Display the list
    print("Enter the elements of second list \n")
    read(b, 5)  # Read the list
    print("The elements of the second list are \n")
    dis(b, 5)  # Display the list
    sort(a, 5)
    print("The sorted list a is:\n")
    dis(a, 5)
    sort(b, 5)
    print("The sorted list b is:\n")
    dis(b, 5)
    merge(a, b, c, 5)
    sort(c, 10)
    print("The elements of merged list are \n")
    dis(c, 10)


def read(c, i):
    for j in range(0, i):
        vals = int(raw_input())
        c.append(vals)


def dis(d, i):
    print(" The list is:\n")
    for j in range(0, i):
        print d[j]
    print "\n"


def sort(arr, k):  # Sorting function , parameters are array and size
    temp = 0
    for i in range(0, k):
        for j in range(0, k - i - 1):
            if (arr[j] < arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def merge(a, b, c, k):  # merge function
    ptra, ptrb, ptrc = 0, 0, 0
    while(ptra < k and ptrb < k):
        if (a[ptra] < b[ptrb]):
            temp = a[ptra]
            c.append(temp)
            ptra = ptra + 1
        else:
            temp = b[ptrb]
            c.append(temp)
            ptrb = ptrb + 1
        # ptrc = ptrc + 1
    while(ptra < k):
        temp = a[ptra]
        c.append(temp)
        ptra = ptra + 1
        # ptrc = ptrc + 1
    while(ptrb < k):
        temp = b[ptrb]
        c.append(temp)
        ptrb = ptrb + 1
        # ptrc = ptrc + 1



if __name__ == '__main__':
    main()