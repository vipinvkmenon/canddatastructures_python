#Chapter 19.5
# Circular Queues

MAX =10


def insert(queue, rear, front, value):  # Insert queue
    rear = (rear+ 1) % MAX
    if(rear == front):
        print("The queue is full can not insert a value\n")
        exit()
    queue[rear] = value
    return queue, rear, front, value

def delete(queue, front, rear, value):  # Delete queue
    if(front == rear):
        print("The queue is empty , cannot delete a value")
        exit()
    front = (front + 1) % MAX
    value = queue[front]
    return queue, front, rear, value

def main():  # Main Function
    queue = [0 for x in range(MAX)]
    front = -1
    rear = -1
    n = 1
    while(n == 1):
        while(n == 1):
            print("Enter the element to be inserted")
            value = int(raw_input())
            queue, rear, front, value = insert(queue, rear, front, value)
            print("Enter 1 to continue")
            n = int(raw_input())
        n = 0
        print("Enter 1 to delete from queue")
        n = int(raw_input())
        while(n == 1):
            queue, front,rear, value = delete(queue, front, rear, value)
            print("The value deleted is " + str(value))
            print("Enter 1 to delete from queue")
            n = int(raw_input())
        n = 0
        print("Enter 1 to continue")
        n = int(raw_input())

main()  # Main Function