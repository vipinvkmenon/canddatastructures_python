#Chapter 1.7
# THE switch STATEMENT

def main():  # Main Function
    i, n = 0, 0  # Variables Declaration nad initialisation
    n = int(raw_input())  # Raw input is for keyboard input
    for i in range(1, n):
        if (i % 2 == 0):
            print("The number " + str(i) + " is even\n")
        else:
            print("The number " + str(i) + " is odd\n")


main()  # Main function entry point