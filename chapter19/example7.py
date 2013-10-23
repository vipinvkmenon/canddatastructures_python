# Chapter 19.6
# APPLICATIONS OF QUEUES
# Priority Queue

class node:

    data = 0
    link = 0
    priority = 0

def insert(front, rear, value, priority):
    temp = node()  # Create a new node using data value passed
    try:
        temp.data = value
        temp.link = None
        temp.priority = priority
        if(rear == None):
            rear = temp
            front = rear
        else:
            if(front.priority < priority):
                temp.link = front
                front= temp
            else:
                if(rear.priority > priority):
                    rear.link = temp
                    rear = temp
                else:
                    temp1 = front
                    while(temp1.link.priority >= priority):
                        temp1 = temp1.link
                        temp.link = temp1.link
                        temp1.link = temp
    except:
        print("The stack is empty can not pop Error")
        exit()
    return front, rear

def delete(front, rear, value, priority):
    try:
        if((front == rear) and (rear == None)):
            print("The queue is empty cannot delete Error\n")
            exit()
        value = front.data
        priority = front.priority
        temp = front
        front =front.link
        if(rear == temp):
            rear = rear.link
    except:
        print("The queue is empty cannot delete Error\n")
        exit()
    return front, rear, value, priority

def main():
    front = None
    rear = None
    n = 1
    while(n == 1):
        while(n == 1):
            print("Enter the element to be inserted and priority\n")
            value = int(raw_input())
            priority = int(raw_input())
            front, rear = insert(front, rear, value, priority)
            print("Enter 1 to continue")
            n = int(raw_input())
        print("Enter 1 to continue")
        n = int(raw_input())
        while(n == 1):
            front, rear, value, priority = delete(front, rear, value, priority)
            print("The value deleted is " + str(value) + " and priority is " +str(priority))
            print("Enter 1 to continue")
            n = int(raw_input())
        print("Enter 1 to continue")
        n = int(raw_input())



main()
