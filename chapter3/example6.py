# Chapter 3.6
# BITWISE OPERATOR

def main():  # Main Function
    #  Variables
    c1, c2, c3 = 0, 0, 0
    print("ENTER VALUES OF c1, c2 AND c3:\n")
    c1 = int(raw_input())
    c2 = int(raw_input())
    c3 = c1 & c2
    print("\n Bitwise AND i.e. c1 & c2 = " + str(c3))
    c3 = c1 | c2
    print("\n Bitwise OR i.e. c1 | c2 = " + str(c3))
    c3 = c1 ^ c2
    print("\n Bitwise XOR i.e. c1 ^ c2 = " + str(c3))
    c3 = ~ c1
    print("\n ones complement of c1 = " + str(c3 + 1))
    c3 = c1 << 2
    print("\n left shift by 2 bits c1 << 2 = " + str(c3))
    c3 = c1 >> 2
    print("\n Right shift by 2 bits c1 << 2 = " + str(c3))




main()
