# Chapter 26.3
#  PROBLEM: CLOSURE OF SETS

MAXLEN = 80
count = 0

def init(answer, slen):
    '''
    /*
     * initialize first slen entries in answer[] to 0.
     */
'''
    for i in range(slen):
        answer[i] = ""
    return answer

def printComb(s, slen, answer, k):
    '''
    /*
     * fixes a character of s and then calls printComb() recursively
     * to get all combinations of the remaining chars.
     */
'''
    global count
    #print("Iterated k is " + str(k) + "s[k] is " + s[k])
    if(s[k] ==""):
        count = count + 1
        an = "".join(answer)
        print(str(count) + ": " + an ),
        return answer
    for i in range(slen - 1):
        if(answer[i] == ""):
            answer[i] = s[k]
            answer = printComb(s, slen, answer, i+1)
            answer[i] = ""
    return answer


def fillBitWise(i, Str, s, slen ):
    '''
    /*
     * the pattern in i is the characteristic function of each char in s.
     * whenever this bit is 1, fill str.
     */
'''
    for j in range(slen):
        if((i & (1<<j)) != 0):
            Str[j] = s[j]
    Str[j] = ""
    #print("".join(Str))
    return Str

def findClosure(s, slen):
    '''
    /*
     * finds closure of chars in s.
     * closure includes all substrings of sizes <= slen.
     * this function also prints their combinations using the
     * function printComb().
     */
'''
    answer = ["" for i in range(MAXLEN)]
    Str = ["" for i in range(MAXLEN)]
    i = (1<<slen)-1
    print(i)
    while(i>=0):
        print("u")
        Str = fillBitWise(i, Str, s, slen)
        print("".join(Str))
        answer = init(answer, len(Str))
        Str2 = "".join(Str)
        print("printComb(" + Str2 + ")")
        printComb(Str, len(Str), answer, 0)
        i = i - 1
        d = raw_input()
        if (d == ""):
            break


def main():
    s =["" for i in range(MAXLEN)]
    print("Enter characters for closure:")
    #t =raw_input()
    t= "Python"
    for i in range(len(t)):
        s[i] = t[i]
    while(s):
        print(len(s))
        findClosure(s, len(s))
        print("Enter characters for closure(press enter to end): ")
        s = ""

main()
