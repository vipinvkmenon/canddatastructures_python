# Chapter 10.2
# SEQUENCE OF EXECUTION DURING  FUNCTION CALL

def main ( ):  # 

    print("1 \n")
    print("2 \n")
    print("3 \n")
    print("4 \n")
    print("5 \n")
    f1 ( )
    print("6 \n")
    print("7 \n")
    print("8 \n")

def f1 ():  

    print("f1-9 \n")
    print("f1-10 \n")
    f2 ( )
    print("f1-11 \n")
    print("f1-12 \n")

def f2 ():

    print("f2-13 \n")
    print("f2-14 \n")
    print("f3-15 \n")

main()  # Main Function Entry


