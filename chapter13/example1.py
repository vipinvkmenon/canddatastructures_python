# Chapter 13.1
# RECURSION


def main():
    m = 2
    k = 3
    i = add(k, m)
    print("The value of addition is " + str(i))

def add(pk, pm):
    if(pm == 0):
        return pk  # A
    else:
        return(1 + add(pk,pm - 1))  # B

main()
