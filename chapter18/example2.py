#Example 18.2
# ADDITION OF THE ELEMENTS OF THE LIST


def main():
    # Variables Declaration
    a = []
    Sum = 0
    print "Enter the elements of the array\n"
    read(a, 5)  # Read the array
    print("The array elements are \n")
    dis(a, 5)  # Display the array
    for i in range(0, 5):  # For loo to find sum
        Sum = Sum + a[i]
    print ("The sum of the elements of the list is " + str(Sum) + "\n")


def read(c, i):  # Read List
    for j in range(0, i):
        vals = int(raw_input())
        c.append(vals)

def dis(c, i):
    for j in range(0, i):
        print c[j]
    print "\n"


main()  # Main Function Entry