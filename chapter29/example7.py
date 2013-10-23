#Chapter 29.7
#  IMPLEMENTATION OF A* ALGORITHM

FALSE = 0
TRUE = 0

def subsetsum(a,n,Sum,selected,startoff):
     #/*
     #* for those elements a[i] which have selected[i] = FALSE,
     #* solve subsetsum problem for sum.
     #* the elements before startoff are of no use.
     #*/
    if(Sum == 0):
        return TRUE
    for i in range(startoff,n):
        if(selected[i] ==FALSE and a[i] <= Sum):
            selected[i]=TRUE
            k, selected =subsetsum(a, n, Sum-a[i], selected, i+1)
            if( k == TRUE):
                return TRUE, selected
            selected[i] =FALSE
    return FALSE, selected

def subsetsumori(a,n, Sum):
    #/*
     #* check whether there is any subset in a[n] having sum sum.
     #*/
    for i in range(n):
        if(a[i] == Sum or (a[i] < Sum and subsetsumori(a+i+1, n-i-1, Sum-a [i]) == 0)):
            print(a[i]),
            return 0
    return 1

def compare(e1, e2):
    #/*
     #* function used in qsort(0).
     #* returns values <0, ==0, >0 if e2 is <el, ==el, >el.
     #* thus we need elements in non-ascending order.
     #*/
    return e2-e1

def printAnswer(a,n,selected):
    #/*
     #* print those a[i] which have selected[i] = TRUE.
     #*/
    for i in range(n):
        if(selected[i] == TRUE):
            print(a[i]),
    print(a[i])


def qsort(List, m, n):  # Quicksort Function
    if(m < n):
        k = getkeyposition(m, n)
        List[m], List[k] = swap(List[m], List[k])
        key = List[m]
        i = m + 1
        j = n
        while (i <= j):
            while ((i <= n) and (List[i] <= key)):
                i = i + 1
            while((j >= m) and (List[j] > key)):
                j = j - 1
            if(i < j):
                List[i], List[j] = swap(List[i], List[j])
        List[m], List[j] = swap(List[m], List[j])
        List = qsort(List, m, j - 1)  # Recursive calls
        List = qsort(List, j + 1, n)
    return List

def swap(x, y):  # swapping functions
    temp = x
    x = y
    y = temp
    return x, y

def getkeyposition(i, j):  # Key position function
    return ((i + j) / 2)

def main():
    a=[5, 3, 4, 8, 9, 6]
    Sum = 15
    size = len(a)
    selected = [FALSE for i in range(size)]
    a=qsort(a, 0,size-1)
    g,selected =subsetsum(a, size, Sum, selected, 0)
    if(g == TRUE):
        printAnswer(a, size, selected)

main()





