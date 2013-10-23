# Chapter 9.1
# Arrays

def main():  # Mian function
    a = []
    for i in range(5):
        a.append(i)
    printarr(a)


def printarr(a):  # Print array function
    for i in range(5):
        print("Value of Array " + str(a[i]))


main()  # Main Function Entry
