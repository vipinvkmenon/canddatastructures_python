#Chapter 18
# MANIPULATIONS ON THE LIST IMPLEMENTED USING AN ARRAY
# INVERSE OF A LIST


def main():
    # Variables Delcaration
    a = []  # input list
    b = []  # inversed resultant
    read(a, 5)  # Read the list
    print ("The array elements are \n")
    dis(a, 5)  # Display the list
    inverse(a, b, 5)  # inverse function list, resultant and size
    # Final Result
    dis(b, 5)  # Display the list


def read(c, i):  # Read List
    print ("Enter the list\n")
    for j in range(0, i):
        vals = int(raw_input())  # read input
        c.append(vals)


def dis(c, i):  # display output
    print(" The list is:\n")
    for j in range(0, i):
        print(c[j])
    print("\n")


def inverse(a, inverse_b, j):  # inverse function
    i, k = 0, 0
    k = j - 1
    for i in range(0, j):
        temp = a[k]
        inverse_b.append(temp)
        k = k - 1


if __name__ == '__main__':
    main()