# Chapter 18.16
#  Implementation of a hash table

SIZE = 50
MAX = 10

class entry:  # Entry Class Serves as the struct
    Next = None
    symbol = []
    value = 0


def hash_value(name):  # Hash Function
    Sum = 0
    i = 0
    while(i < len(name)):
        Sum =  Sum + ord(name[i])  # Sum + ASCII val
        i = i + 1
    return Sum % SIZE


def initialize(table):  # Table initializes
    i = 0
    for i in range(0, SIZE):
        table[i] = None

def insert(table, name, val):  # Insert to table
    flag = 1
    h = hash_value(name)
    temp = table[h]
    while (temp is not None and flag):
        if(temp.symbol == name):
            print("The symbol " + name + " is aldready present in table")
            flag = 0
        temp = temp.Next
    if (flag == 1):
        temp = entry()
        if (temp is None):
            print("ERRRR..........\n")
            exit()
        temp.symbol = name
        temp.value = val
        table[h] = temp


def retrieve(table, name):  # Retrieve from table
    flag= 1
    h = hash_value(name)
    temp = table[h]
    while(temp is not None and flag):
        if(temp.symbol == name):
            print("The symbol " + name + " is present in the table "),
            print("having value " + str(temp.value))
            flag= 0
        temp = temp.Next
    if(flag == 1):
        print("The symbol " + name + " is not present in the table")

def main():
    # Variable Declaration
    table = [None for x in range(SIZE)]
    name,value,n = 0, 0, 1
    initialize(table)
    while(n == 1):
        while(n == 1):
            print("Enter the symbol and value pair to be inserted\n")
            name = raw_input()
            value = int(raw_input())
            insert(table, name, value)
            print("Enter 1 to continue")
            n = int(raw_input())
        n = 1
        while(n == 1):
            print("Enter the symbol whose value is to be retrieved\n")
            name = raw_input()
            retrieve(table, name)
            print("Enter 1 to continue")
            n = int(raw_input())  # if 1 will retirieve / search
        n = 1
        print("Enter 1 to continue")
        n = int(raw_input())  # If one will go back to insert


main()







