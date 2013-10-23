# Chapter 10.4
# CALL BY REFERENCE

def main():  #Main Function
    i = [0]
    print("The value of i before call " + str(i[0]))
    f1(i)  # Call f1
    print("The value of i after call " + str(i[0]))

def f1(k):  # f1 function
    k[0] = k[0] + 10


main()  # Main Function Entry
