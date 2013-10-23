# Chapter 13.3
#WRITING A RECURSIVE FUNCTION

def main():  # Main Function
    k = 4
    i = fact(k)
    print("The value of i is " + str(i))

def fact(n):  # Factorial Function
    if(n <= 0):
        return(1)
    else:
        return(n*fact(n - 1))

main()  # Main Function Entry

    
