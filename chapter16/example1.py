# Chapter 16.1
# UNION

from ctypes import *

class marks(Union):  # A
    _fields_ = [("perc",c_float), ("grade", c_char)]  # B C

def main():
    student1 = marks() # E
    student1.perc = 98.5 # F
    print("Marks are " + str(student1.perc) + " Address is " + str(id(student1.perc))) # g
    student1.grade = "A"  # H
    print("Grade is " + str(student1.grade) + " Address is " + str(id(student1.grade)))  # I
    

main()

    
