# Chapter 11.1
# STORAGE
i = 1
def main():
    global i
    i = 1
    f1()
    print("after first call \n")
    f1()
    print("after second call \n")
    f1()
    print("after second call \n")
    


def f1():  #f1 function
  if not hasattr(f1, "k"):  # To check if attribute exist
     f1.k = 0  # it doesn't exist yet, so initialize it  this is the static variable
  j = 10
  f1.k += 10
  print("value of k " + str(f1.k) + " j " + str(j))

main()
