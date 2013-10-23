# Chapter 26.6
# IMPLEMENTATION OF THE SOUNDEX FUNCTION

MAXLEN = 80
NALPHA = 26

soundexGroups = ["aeiouhyw", "kcgjqsxz", "td", "bpfv", "l", "mn", "r"]

soundexCodes = ["" for i in range(NALPHA)]

def soundexInit():
    """
    /*
     * build an inverted index from the global table soundexGroups[].
     * the inverted index is stored in global soundexCodes[].
     */"""
    g = 0
    global soundexGroups
    global soundexCodes
    for i in range(len(soundexGroups) - 1, -1, -1):
        sptrstr = soundexGroups[i]
        sptr = ["" for i in range(len(sptrstr)+1)]
        for i in range(len(sptrstr)):
            sptr[i] = sptrstr[i]
        g = 0
        while(sptr[g] != ""):
            soundexCodes[ord(sptr[g]) - ord("a")] = i
            g = g + 1

def compareCodes(soundex1, soundex2):
    ptr1 = soundex1
    ptr2 = soundex2
    g = 0
    while(ptr1[g] != -1 and ptr2[g] != -1 and ptr1[g] == ptr2[g]):
        g = g + 1
    if(ptr1[g] ==ptr2[g]):
        return 1
    else:
        return 0

def findSoundex(s, soundex, lastchar, g, h):
    '''/*
     * find the soundex code for s and save in soundex.
     * the stored value is the index in the array of soundex codes.
     * function is recursive.
     * start by changing multiple occurrences of chars in consecutive positions
     * by single occurrences.
     * end soundex by -1.
     * lastchar == -1 implies this is the first call to this function.
     */'''
    global soundexGroups
    global soundexCodes
    if(s[g] == ""):
        soundex[h] = -1
        lastchar = ""
    elif(s[g] == lastchar):
        s, soundex = findSoundex(s, soundex, lastchar, g+1, h)
    elif(lastchar ==-1): # *s is the first char.
        soundex[h] = soundexCodes[ord(s[g]) - ord("a")]
        s, soundex = findSoundex(s, soundex, s[g], g+1, h+1)
    elif(soundexCodes[ord(s[g]) - ord("a")] == 0):
        s, soundex = findSoundex(s, soundex, s[g], g+1,h)
    else:
        soundex[h] = soundexCodes[ord(s[g]) - ord("a")]
        s, soundex = findSoundex(s, soundex, s[g], g+1, h+1)
    return s, soundex

def compareSoundex(s1, s2):
    """
    /*
     * find soundex codes for s1 and s2.
     * return 1 if codes are equal else 0.
     */"""
    soundex1 = [0 for i in range(MAXLEN)]
    soundex2 = [0 for i in range(MAXLEN)]
    s1, soundex1 = findSoundex(s1, soundex1, -1, 0, 0)
    s2, soundex2 = findSoundex(s2, soundex2, -1, 0, 0)
    return compareCodes(soundex1, soundex2)

def main():
    s1 = ["" for i in range(MAXLEN)]
    s2 = ["" for i in range(MAXLEN)]
    soundexInit()
    print("Enter string 1")
    #t = raw_input()
    t = "Rail"
    for i in range(len(t)):
        s1[i] = t[i]
    g = 1
    while(g == 1):
        print("Enter string 2")
        #t = raw_input()
        t = "rail"
        for i in range(len(t)):
            s2[i] = t[i]
        v = "".join(s1)
        p = "".join(s2)
        print("(" + v + " == " + p + ")= " + str(compareSoundex(s1, s2)))
        print("Enter string 1(enter to end): ")
        g = 0

main()


