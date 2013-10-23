# Chapter 15.1
#  Structures

class student: # A
    name = 0  # B
    marks = 0  # C
student1 = student()  # D
student2 = student()
def main():
    student3 = student() # e
    s1 = raw_input() # f h
    f = float(raw_input()) # h i
    student1.name = s1  # J
    student2.marks = f  # K
    print("Name is  " + student1.name)  # L
    print("Mark is " + str(student2.marks))  # M


main()  # Main Function Entry

    
