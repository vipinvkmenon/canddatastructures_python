# Chapter 15.2
# COMPLEX STRUCTURE DEFINITIONS

class address:
    plot = 0
    street = 0
    city = 0

class student:
    name = 0
    marks = 0
    adr = address()

def main():
    student1 = student()
    Class = [student() for x in range(20)]
    Class[1].marks = 70
    Class[1].name= "Anil"
    Class[1].adr.plot = "7 "
    Class[1].adr.street = "Mg Road"
    Class[1].adr.city = "Mumbai "


    print( " Marks are " + str(Class[1].marks))
    print( " name are " + Class[1].name)
    print( " adr.plot is " + Class[1].adr.plot)
    print( " adr.street is " + Class[1].adr.street)
    print( " adr.city is " + Class[1].adr.city)

main()
