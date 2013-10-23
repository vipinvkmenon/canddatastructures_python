# Chapter 13.2
# STACK OVERHEADS IN RECURSION

global old
global current

def main():
    global old
    global current
    global j
    j = 0
    old = 0
    current = 0
    k = 4
    i = fact(k)
    print("The value of i is " + str(i))
    diff = old - current
    print("stack overheads are " + str(diff))

def fact(n):
    global old
    global current
    global j
    j = 0
    if not hasattr(fact,"m"):
        fact.m = 0
    if(fact.m == 0):
        old = id(j)
    else:
        j = j + 0
        current = id(j)
    fact.m = fact.m + 1
    print("the address of j and m is " + str(id(j)) + " " + str(id(fact.m)))
    if(n<=0):
       return(1)
    else:
       return(n*fact(n-1))


main()
