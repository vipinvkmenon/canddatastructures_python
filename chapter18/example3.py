#Example 18.3
# ADDITION OF TWO LISTS



def main():
    # Variable Declaration
    a,b,c=[] , [] , []
    i = 0
    print "Enter the elements of the first list\n"
    read(a, 5)  # Read the List
    print ("The elements of first list are :\n")
    dis(a, 5)  # Display the List
    print "Enter the elements of the second list\n"
    read(b, 5)  # Read the List
    print ("The elements of second list are :\n")
    dis(b, 5)  # Display the List
    add(a, b, c, i)
    print ("The resultant list is:\n")
    dis(c, 5)


def add(a, b, c, i):  #  Addition Fuction
    for i in range (0, 5):
        Sum = a[i] + b[i]
        c.append(Sum)

def read(c , i):  # Read List
    for j in range(0 ,i):
        vals = int(raw_input())
        c.append(vals)

def dis (c, i):  # Display Function
    for j in range (0, i):
        print (c[j]),
    print "\n"


main()  # Main Function Entry