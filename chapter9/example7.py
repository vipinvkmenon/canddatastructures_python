#Chapter 9.7
# Three Dimension Array

def main():  # Main Function
    a = [[[0 for x in xrange(2)] for x in xrange(3)] for x in xrange(4)]  # 3D Array
    b = [[0 for x in xrange(3)] for x in xrange(4)]  # 2D array
    c = [0 for x in xrange(4)]
    cnt = 0
    for i in range(4):
        for j in range(3):
            for k in range(2):
                a[i][j][k] = cnt
                cnt += 1
    print_threedim(a)
    
def print_onedim(a):  # One dimension array print
    for i in range(4):
        print(str(a[i]) + "     "),
    print("\n")
def print_twodim(a):  # two dimension array print
    for j in range(3):
        print_onedim(a)

def print_threedim(a): # One dimension array print
    for j in range(2):
        print_twodim(a)
    print("\n")


main()





                
    
    
