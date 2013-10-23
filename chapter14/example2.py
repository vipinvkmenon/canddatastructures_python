# Chapter 14.2
# STRING DEFINITION

def main():
    s1 = "abcd"
    s2 = "efgh"
    print(s1 + " " + str(id(s1)))
    print(s2 + " " + str(id(s2)))
    s1= s2
    print(s1 + " " + str(id(s1)))
    print(s2 + " " + str(id(s2)))
    

main()
