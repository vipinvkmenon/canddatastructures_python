# Chapter 19.1
# Array Implementation of a Stack 1

MAX = 10

def push(stack, top, value):  # push function
    if(top < MAX):
        top = top + 1
        stack[top] = value
    else:
        print("Stack is full cannot push a value")
        exit()
    return stack, top

def pop(stack,top, value):  # pop function
    if(top >= 0):
        value = stack[top]
        top = top - 1
    else:
        print("Stack is empty cannot pop a value")
        exit()
    return value, top

def main():
    stack = [0 for x in range(MAX)]
    top = -1
    n = 1
    while (n == 1):
        while(n == 1):
            print("Enter the element to be pushed")
            value = int(raw_input())
            stack, top = push(stack, top, value)
            print("Enter 1 to continue")
            n = int(raw_input())
        print(" Enter 1 to pop element")
        n = int(raw_input())
        while(n == 1):
            value, top = pop(stack,top,value)
            print("The value popped is " + str(value))
            print(" Enter 1 to pop element")
            n = int(raw_input())
        print("Enter 1 to continue")
        n = int(raw_input())

main()
        
        
        
