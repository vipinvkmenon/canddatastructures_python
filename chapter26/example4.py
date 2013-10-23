# Chapter 26.4
#  DISTANCE BETWEEN TWO STRINGS

MAXLEN = 80

def findMin(d1, d2, d3):
    """
    /*
    * return min of d1, d2 and d3.
    */"""
    if(d1 < d2 and d1 < d3):
        return d1
    elif(d1 < d3):
        return d2
    elif(d2< d3):
        return d2
    else:
        return d3

def findEditDistance(s1, s2,i,j):
    """
    /*
     * returns edit distance between s1 and s2.
     */"""
    d1 = d2 = d3 = 0
    if (i >= len(s1) or j >= len(s2)):
        return 0
    if(s1[i] == ""):
        return len(s2)
    if(s2[j] == ""):
        return len(s1)
    if(s1[i] == s2[j]):
        d1 = findEditDistance(s1, s2, i + 1, j+ 1)
    else:
        d1 = 1 + findEditDistance(s1, s2,i+1, j+1)  # update.
        d2 = 1+findEditDistance(s1, s2, i, j+ 1)                  # insert.
        d3 = 1+findEditDistance(s1, s2, i + 1, j)
    return (findMin(d1, d2, d3))

def main():
    s1 = ["" for i in range(MAXLEN)]
    s2 = ["" for i in range(MAXLEN)]
    #print("Enter String 1")
    #s1 = raw_input()
    t = "sack"
    for i in range(len(t)):
        s1[i] = t[i]
    a = "".join(s1)
    g = 1
    while(g == 1):
        #print("Enter String 2")
        #s2 = raw_input()
        t = "back"
        for i in range(len(t)):
            s2[i] = t[i]
        b = "".join(s2)
        print("Edit distance(" + a + ", " + b + ")" + str(findEditDistance(s1, s2, 0, 0)))
        print("Enter string 1(enter to end):")
        g = 0

main()
