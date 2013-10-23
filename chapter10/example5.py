# Chapter 10.5
# GLOBAL VARIABLES
i = 0
def main():  # Main Function
    global i
    f1()
    i = 0
    print(" value of i in main " + str(i))
    f1()
    print(" value of i after call in main " + str(i))

def f1():
    global i
    i = 50


main()
    
