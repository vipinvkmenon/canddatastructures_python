# Chapter 26.5
# FINDING THE MAXIMUM MATCHING PATTERN IN THE STRING

MAXLEN = 80

def findMaxPat(s, pat, maxpat):
    i = 0
    j = 0
    k = 0
    while(s[i] != "" and pat[j] != ""):
        if(s[i] == pat[i]):
            maxpat[k] = i
            k = k + 1
            j = j + 1
        i = i + 1
    if(pat[j] == "" ):
        print("whole pat found.")
    else:
        print("whole pat NOT found")
        maxpat[k] = -1
    return maxpat

def printMaxPat(s, maxpat):
    sptr = s
    i = j = 0
    while(sptr[i] != "" and maxpat[j] != -1):
        if(ord(sptr[i]) - ord(s[i]) == maxpat[j]):
            print("^")
            j = j + 1
        else:
            print(" ")
        i = i + 1
    print("\n")

def main():
    s = ["" for i in range(MAXLEN)]
    pat = ["" for i in range(MAXLEN)]
    maxpat = ["" for i in range(MAXLEN)]
    print("Enter main string")
    #t = raw_input()
    t = "watermelon"
    for i in range(len(t)):
        s[i] = t[i]
    g = 1
    while(g == 1):
        print("Enter pattern to be searched: ")
        #t = raw_input()
        t = "water"
        for i in range(len(t)):
            pat[i] = t[i]
        maxpat = findMaxPat(s, pat, maxpat)
        printMaxPat(s, maxpat)
        print("Enter main string: ")
        #d = raw_input()
        g = 0

main()

