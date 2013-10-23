# Chapter 24.2
# IMPLEMENTATION OF TWO STACKS USING AN ARRAY

N = 10
EINDEXOUTOFBOUND = -1
SUCCESS = 0
global twostacks
twostacks = [0 for i in range(N)]
global stop1
global stop2
stop1 = -1
stop2 = N

def sPush(stacki, data):
    #  pushes data on top of stacki.
    # returns error on overflow.
    global stop1
    global stop2
    global twostacks
    if(stop2 - stop1 == 1):
        return EINDEXOUTOFBOUND
    if(stacki == 1):
        stop1 = stop1 + 1
        twostacks[stop1] = data
    else:
        stop2 = stop2 - 1
        twostacks[stop2] = data
    return SUCCESS

def sDelete(stacki):
    # deletes element at top from stacki.
    global stop1
    global stop2
    print("deleting from stack")
    if(stacki == 1):
        if(stop1 >= 0):
            stop1 = stop1 - 1
        else:
            return EINDEXOUTOFBOUND
    else:
        if(stop2 < N):
            stop2 = stop2 + 1
        else:
            return EINDEXOUTOFBOUND
    return SUCCESS

def sPrint():
    # prints the two stacks
    global stop1
    global stop2
    global twostacks
    for i in range(stop1+1):
        print(twostacks[i]),
    print(": "),
    for i in range(stop2, N):
        print(twostacks[i]),
    print("\n")

def main():
    sPush(1,1)
    sPush(2,1)
    sPush(1,4)
    sPush(2,5)
    sPrint()
    sDelete(2)
    sDelete(2)
    sPrint()
    sDelete(2)
    sDelete(1)
    sDelete(1)
    sDelete(1)
    sPrint()
    sPush(2,2)
    sPush(1,9)
    sPrint()
    sDelete(1)
    sPrint()
    sDelete(2)
    sPrint()
    sPush(2,0)
    sPush(1,5)
    sPush(1,3)
    sPrint()
    sDelete(2)
    sPrint()




main()


