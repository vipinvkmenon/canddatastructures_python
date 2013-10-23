# Chapter 8.11
# macro and functions


def add(x1, x2):
    return x1 + x2

def mult(x1, x2):
    return x1 * x2

def main():
    a = 2
    b = 3
    c = 4
    d = 5
    e = mult(add(a, b), add(c, d))
    print("The value of e is " + str(e))


main()
