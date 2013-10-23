# Chapter 15.3
# PROGRAMMING WITH STRUCTURES

class student:
    name = 0
    marks = 0

def main():
    student1 = student()
    student1 = read_student()
    print_student(student1)
    read_student_p(student1)
    print_student(student1)

def read_student():  # A
    student2 = student()
    student2.name=raw_input()
    student2.marks = int(raw_input())
    return student2

def print_student(student2):  # B
    print("name is " + student2.name)
    print("marks are " +str(student2.marks))
    
def read_student_p(student2):  # C
    student2.name=raw_input()
    student2.marks = int(raw_input())

main()

    
