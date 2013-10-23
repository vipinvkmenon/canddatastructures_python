# Chapter 26.1
#  MAXIMIZE A COMBINATION UNDER CONSTRAINTS

NANSWERS = 3
MAXCONS = 5

FALSE = 0
TRUE = 1

def isAbsent(strnum, answer, nans):
    # returns TRUE if answer[nans] does NOT contain strnum.
    for i in range(nans):
        if(answer[i] == strnum):
            return FALSE
    return TRUE

def satisfies(answer, nans, constraints, ncons):
    '''
    /*
    * returns TRUE if nans answers in answer satisfy ncons constraints.
    * note that each constraint ends with -1.
    */
'''
    for i in range(ncons):
        j = 0
        while(constraints[i][j] != -1):
            if(isAbsent(constraints[i][j], answer, nans) == TRUE):
                break
            j = j + 1
        if(constraints[i][j] == -1):
            return FALSE
    return TRUE

def findMaxComb(lengths, nstr, constraints, ncons, answer, nans, maxsum, startstr, startans, currsum):
    '''
     /*
    * find the max sum of lengths of nans strings out of nstr strings of
    * lengths lengths[] satisfying ncons constraints constraints[].
    * save the max sum in *maxsum and the string indices in answer[].
    */
'''
    if(startans < nans):
        for i in range(startstr,nstr):
            answer[startans] = i
            maxsum= findMaxComb(lengths, nstr, constraints, ncons, answer, nans, maxsum, i+1, startans+1, currsum+lengths[i])
    elif(currsum > maxsum):
        if(satisfies(answer, nans, constraints, ncons) == TRUE):
            maxsum = currsum
    return maxsum

def main():
    lengths = [9, 8, 6, 5, 4, 3]  # lengths[i] = length(string[i]
    answer = [0 for i in range(15)]
    constraints = [[1,3,-1],[2,-1],[1,5,-1],[3,4,-1],[0,4,5,-1], [0,4,-1], [0,3,5,-1]]
    ncons = len(constraints)
    nstr = len(lengths)
    maxsum = 0
    for i in range(1, NANSWERS+1):
        maxsum= findMaxComb(lengths, nstr, constraints, ncons, answer, i, maxsum, 0, 0, 0)
        print("After " + str(i) + " strings : maxsum = " + str(maxsum))

main()
