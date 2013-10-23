# Chapter10.6
# RESOLVING VARIABLE REFERENCES

i = 0  # global cariable A
def main():  # Main Function
    global i
    f1() # C
    i = 0  # local variable D
    print("value of i in main " + str(i))  # E
    f1()  # F
    print("value of i after call " + str(i)) # G


def f1():  # H
    i = 50  #I,J


main() #Main Function
    
    
