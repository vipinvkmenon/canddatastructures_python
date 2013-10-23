# Chapter 25.3
# REVERSING LINKS IN THE CASE OF CIRCULAR LIST

SUCCESS = 0
ERROR = -1

class node:

    def __init__(self):
        self.data= 0
        self.next = None

head = None

def lInsert(data):
    # inserts a new node containing data at start of the list.
    ptr = node()
    ptr.data = data
    global head
    if(head == None): # this is the first element in the list.
        ptr.next = ptr
        head = ptr
    else:
        ptr.next = head.next
        head.next= ptr
    return SUCCESS

def lPrint():
    global head
    if(head == None):
        return 0
    else:
        print(head.data),
        ptr = head.next
        while(ptr != head):
            print(ptr.data),
            ptr = ptr.next
        print("\n")

def lReverse():
    #insitu reverses the list
    print("reversing the list...")
    if(head == None):
        return SUCCESS
    prev = head
    curr =prev.next
    Next = curr.next
    while(curr != head):
        curr.next = prev
        prev = curr
        curr = Next
        Next = Next.next
    head.next = prev
    return SUCCESS

def main():
    lPrint()
    lInsert(1)
    lPrint()
    lInsert(2)
    lInsert(3)
    lInsert(4)
    lInsert(5)
    lInsert(6)
    lPrint()
    lReverse()
    lPrint()



main()
