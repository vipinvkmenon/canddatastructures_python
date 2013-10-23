# Chapter 8.9
# #line

import inspect  # Importo inspect

def main():
    print("A")
    print("B")
    __FILE__ = inspect.getfile(inspect.currentframe())  # Get name of current file
    __LINE__ = inspect.currentframe().f_back.f_lineno
    print("C FILE " + __FILE__ + " LINE " + str(__LINE__))  # Get line number
    print("E")
    print("F")

main()