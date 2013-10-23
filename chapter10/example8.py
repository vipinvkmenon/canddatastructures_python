# Chapter 10.8
# CALLING FUNCTION case 2

def f1(k):
    k[0] = k[0] + 10
    
def main():
    i = [0]
    print("The value of i before call " + str(i[0]))
    f1(i)  # Call f1
    print("The value of i after call " + str(i[0]))




main()

    
    
    


