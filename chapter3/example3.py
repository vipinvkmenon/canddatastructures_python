#Chapter 3.3
# LOGICAL OPERATOR

def main():  # Main Function
    #  Variables
    c1, c2, c3 = 0, 0, 0
    print("ENTER VALUES OF c1, c2 AND c3:\n")
    c1 = int(raw_input())
    c2 = int(raw_input())
    c3 = int(raw_input())
    if((c1 < c2) and (c1 < c3)):
        print("c1 is less than c2 and c3\n")
    if(not (c1 < c2)):
        print("c1 is greater than c2")
    if((c1 < c2) or (c1 < c3)):
        print("c1 is less than c2 or c3 or both")


main()  # Main Function Entry



