def g(x):
    x[0]=10
    return x

def h(j):
    k=j
    k=g(k)
    return j

def gg():
    hh=[0]
    print hh
    hh = h(hh)
    print hh

gg()
