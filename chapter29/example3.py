#Chapter 29.3
#  ALL COMBINATIONS OF STRINGS

MAXLEN = 80
count = 0
j = 0

def init(answer, slen):
    # initialize first slen entries in answer[]  to 0.
    for i in range(slen):
        answer[i] = ""
    return answer

def printComb(s, slen, answer):
    #/*
     #* fixes a character of s and then calls printComb0 recursively
     #* to get all  combinations of the remaining chars.
     #*/
    global count
    global j
    if(s[j] == ""):
        count = count + 1
        print(count),
        print("".join(answer))
        return s, answer
    for i in range(slen):
        if(answer[i] == ""):
            answer[i] = s[j]
            j = j+1
            s, answer = printComb(s,slen,answer)
            answer[i] = 0
    return s, answer

def main():
    s = ["" for i in range(MAXLEN)]
    answer = ["" for i in range(MAXLEN)]
    print("Enter  characters for combination: ")
    #d = raw_input()
    d = "Hello"
    g = " "
    for i in range(len(d)):
        s[i] = d[i]
    #while(g != ""):
    answer = init(answer,len(d))
    s, answer = printComb(s, len(d), answer)
    print("Enter characters for combination(press enter to end): ")
    #s = raw_input()
        #g = ""

main()



