#Chapter 1.4
# THE CONTROL STATEMENT (if STATEMENT)


def main():  # Main Function
    # Variables Declaration
    i, j, big = 0, 0, 0  # Initialised
    i = int(raw_input())  # Raw input is for keyboard input
    j = int(raw_input())
    big = i
    if (big < j):
        big = j
    print("The biggest of the two numbers is "),
    print(big)
    if (i < j):  # if condition
        big = j
    else:  # Else condition
        big = i
    print("The biggest of the two numbers (using else) is "),
    print(big)



main()  # Main function entry point