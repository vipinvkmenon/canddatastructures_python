# Chapter 14.2
# STRINGS AS PARAMETERS


def main(): # Main Fuction
    s1 = "abcde"
    cnt = 0
    cnt = cnt_str(s1)
    print("total characters are  " + str(cnt))

def cnt_str(s1):  # Counter
    cn = 0
    for x in s1:
        cn = cn + 1
    return cn
main()  # Main Function Entery
