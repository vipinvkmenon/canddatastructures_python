# Chapter 17.1
# THE CONCEPT OF FILES

# Soting Function
def bubble(x, n):
    
    for Pass in range(n - 1):
            for j in range((n - (Pass +1))):
                if (x[j] > x[j + 1]):
                    switched = 1
                    hold =  x[j]
                    x[j] = x[j + 1]
                    x[j + 1] = hold
    return x

# File Write Function
def filewrite():
    fp = open("student.txt",'a')
    print("ENTER ROLL NUMBER, NAME, MARKS")
    ch = 1
    while(ch == 1):
        roll = int(raw_input())
        name = raw_input()
        mark = int(raw_input())
        fp.write(str(roll) + " " + name + " " + str(mark) + "\n")
        print("Press 1 to continue")
        ch = int(raw_input())
    fp.close()


# Output Data on screen

def fileprint():
    fp = open("student.txt",'r')
    i = 0
    print("ROLL NUMBER, NAME, MARKS")
    print(fp.read())
    fp.close()
    print("\nnPRESS ANY KEY")
    d = raw_input()

# File Sorting
def filesort():
    fp = open("student.txt", 'r')
    fm = open("marks.txt", 'w')
    marks = []
    rollno = []
    name = []
    i = 0
    x = []
    lines=fp.readlines()
    lineslist = []
    for j in range(len(lines)):
        lineslist.append(lines[j].split())
    i = len(lines)
    for j in range(len(lineslist)):
        rollno.append(lineslist[j][0])
        name.append(lineslist[j][1])
        marks.append(lineslist[j][2])
        x.append(lineslist[j][2])

   
    n = i
    x = bubble(x,n)

    for i in range(n):
        print(x[i])
    for i in range(n):
        for j in range(n):
            if(x[i] == marks[j]):
                fm.write(str(rollno[j]) + " " + name[j] + " " + str(marks[j]) + "\n")
    fm.close()
    fp.close()
    print("\nnPRESS ANY KEY")
    d = raw_input()

# DATA USING ROLLNO
def rollin():
    fm = open("marks.txt", 'r')
    print("\nEnter Roll No")
    roll1=int(raw_input())
    i = 0
    marks = []
    rollno = []
    name = []
    x = []
    lines = fm.readlines()
    lineslist = []
    for j in range(len(lines)):
        lineslist.append(lines[j].split())
    i = len(lines)
    for j in range(len(lineslist)):
        if (roll1 == int(lineslist[j][0])):
            print("Roll No.  NAME  MARKS\n")
            print(str(lineslist[j][0]) + "  " + lineslist[j][1] + "  " + str(lineslist[j][2]))
            break
        i = i + 1
        
    
def avgmarks():  # Average Marks
    fm = open("marks.txt", 'r')
    i = 0
    marks = []
    rollno = []
    name = []
    x = 0
    lines = fm.readlines()
    lineslist = []
    for j in range(len(lines)):
        lineslist.append(lines[j].split())
    i = len(lines)
    for j in range(len(lineslist)):
        x = x + float(lineslist[j][2])
    n=i
    avg= float(x / n)
    print("AVERAGE MARKS OF %d STUDENTS ARE " +str(avg))
    fm.close()
    print("\nPress any key")
    d = raw_input()    
                
    
def main():
    c = 0
    while(c != 6):
        print("GIVE CHOICE--\n")
        print("   1 TO ENTER STUDENT INFO.\n")
        print("   2 TO SEE STUDENT.TXT FILE\n")
        print("   3 TO SORT FILE ON BASIS OF MARKS\n")
        print("   4 TO PRINT STUDENT INFO. USING ROLL NO\n")
        print("   5 TO FIND AVERAGE OF MARKS\n")
        print(" 6 TO EXIT\n\n--")
        c = int(raw_input())
        if( c == 1):
            filewrite()
        elif(c == 2):
            fileprint()
        elif(c == 3):
            filesort()
        elif(c == 4):
            rollin()
        elif(c == 5):
            avgmarks()
        else:
            break
            
            
            
main()
        
        
        
    
    
    
    
    
    
