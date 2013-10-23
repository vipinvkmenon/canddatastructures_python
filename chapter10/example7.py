# Chapter 10.7
# CALLING FUNCTION case 1

def main():
    i = [0]
    print("The value of i before call " + str(i[0]))
    f1(i)  # Call f1
    print("The value of i after call " + str(i[0]))

def f1(k):
    k[0] = k[0] + 10


main()

    
    
    


