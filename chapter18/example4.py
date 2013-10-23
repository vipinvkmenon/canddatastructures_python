#Chapter 18.4
# MANIPULATIONS ON THE LIST IMPLEMENTED USING AN ARRAY
# INVERSE OF A LIST


def main():
    # Variable Declarations
    a = []
    read(a, 5)  # Read the array
    print ("The array elements are \n")
    dis(a, 5)  # Display the array
    inverse(a, 5)
    # Final Result
    dis(a, 5)  # Display the array


def read(c, i):
    print "Enter the list\n"
    for j in range(0, i):
        vals = int(raw_input())
        c.append(vals)


def dis(c, i):
    print(" The list is:\n")
    for j in range(0, i):
        print c[j]
    print "\n"


def inverse(inver_a, j):  # Function to inverse the array
    i, temp = 0, 0  # Variable Declarations
    j = j - 1
    for i in range(0, j / 2):
        temp = inver_a[i]
        inver_a[i] = inver_a[j]
        inver_a[j] = temp
        j = j - 1

main()  # Main Function Entry