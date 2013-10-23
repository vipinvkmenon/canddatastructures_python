# Chapter 14.1
# STRINGS AS AN ARRAY OF CHARACTERS

def main():
    cnt = 0
    s1 = "Hello" # A B
    print(s1)  # C
    s2 = ["H","e","l","l","o"]  # D
    print("".join(s2))  # E
    s = []
    for x in s1:
        s.append(x)
    s1 = s
    print("".join(s1))
    s1 = []
    ch = raw_input()
    for x in ch: # F G H
            if (x != "#"):
                s1.append(x)
    print("".join(s1))
        

main()  # Main function entry

    
    
