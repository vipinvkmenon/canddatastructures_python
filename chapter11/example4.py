# Chapter 11.4
# Scope of variables

def main():
    i = 10
    in_block()
    print("value of i is " + str(i))

def in_block():
    for i in range(2):
        print("value of i is " + str(i))
    


main()
