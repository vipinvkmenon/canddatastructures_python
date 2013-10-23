# Chapter 19.2
# Stack Implementation of a Stack

class node:
    data = 0
    link =0

def push(p, value):
    temp = node()  # Create new node
    try:
        temp.data = value
        temp.link = p
        p = temp
    except:
        print("The stack is empty can not pop Error")
        exit()
        exit
    return(p)
def pop(p, value):

    try:
        value = p.data
        temp = p
        p = p.link
        return p, value
    except:
        print("The stack is empty can not pop Error")
        exit()
def main():
    n = 1
    top = 0
    value = 0
    while(n == 1):
        while(n == 1):
            print("Enter the element to be pushed")
            value = int(raw_input())
            top = push(top, value)
            print("Enter 1 to continue")
            n= int(raw_input())

        print("Enter 1 to pop element")
        n= int(raw_input())
        while(n == 1):
            top, value = pop(top, value)
            print("The value popped is " +str(value))
            print("Enter 1 to pop element")
            n= int(raw_input())
        print("Enter 1 to pop element")
        n= int(raw_input())

main()





