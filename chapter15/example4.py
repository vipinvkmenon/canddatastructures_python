# Chapter 15.3
# STRUCTURE POINTERS

class student:  #A
    name = 0  # B
    marks = 0  #C

def main():
   
    student2 = student() # F
    student1 = student2 # E G

    name = raw_input() # H
    marks=float(raw_input()) # I

    student1.name = name # J
    student2.marks = marks  # K

    print("Name is " + student1.name) # L 
    print("Marks are " + str(student2.marks))  # M  

main()
