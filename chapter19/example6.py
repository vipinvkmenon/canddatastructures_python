# Chapter 19.6
# IMPLEMENTATION OF A QUEUE USING LINKED REPRESENTATION

class node:

    data = 0
    link = 0

def insert(front, rear, value):
    temp = node()  # Create a new node using data value passed
    try:
        temp.data = value
        temp.link = None
        if(rear == None):
            rear = temp
            front = rear
        else:
            rear.link = temp
            rear = temp
    except:
        print("The stack is empty can not pop Error")
        exit()
    return front, rear

def delete(front, rear, value):
    try:
        if((front == rear) and (rear == None)):
            print("The queue is empty cannot delete Error\n")
            exit()
        value = front.data
        temp = front
        front =front.link
        if(rear == temp):
            rear = rear.link
    except:
        print("The queue is empty cannot delete Error\n")
        exit()
    return front, rear, value

def main():
    front = None
    rear = None
    n = 1
    while(n == 1):
        while(n == 1):
            print("Enter the element to be inserted\n")
            value = int(raw_input())
            front, rear = insert(front, rear, value)
            print("Enter 1 to continue")
            n = int(raw_input())
        print("Enter 1 to continue")
        n = int(raw_input())
        while(n == 1):
            front, rear, value = delete(front, rear, value)
            print("The value deleted is " + str(value))
            print("Enter 1 to continue")
            n = int(raw_input())
        print("Enter 1 to continue")
        n = int(raw_input())



main()
