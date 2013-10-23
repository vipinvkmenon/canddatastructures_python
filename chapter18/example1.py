#Example 18.1
# Implementing a list with operations for reading valuse and listing them


def main(): #Main Function
    # Variables Declared
    a=[]
    print "Enter the elements of the array\n"
    read (a , 5) # Read the array
    print ("The array elements are \n")
    # Final Output
    dis (a, 5)  # Display the array



def read(c , i):  # Read Array
    for j in range(0 ,i):
        vals=int ( raw_input () )
        c.append (vals)


def dis (c , i):  # Display the array
    for j in range (0 , i):
        print c[j],
    print "\n"


main()  # Main function Entry
