# Chapter 10.3
#Parameter Passing

def main():  # Main Function
    i = 0
    print("The value of i before call " + str(i))
    f1(i)
    print("The value of i after call " + str(i))


def f1(k):  # Function f1
    k = k +1


main()  # Main Function entry
    
