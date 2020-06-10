# CS1210 Spring 2017 HW2 solutions

#1
def printRanges(high, low):
    current = high
    while current >= low:
        print(current)
        rangeNum = 0
        while (rangeNum < current):
            print(rangeNum, end = " ")
            rangeNum = rangeNum + 1
        print()
        current = current - 1
        
#2    
def printVowelStats(inputString):
    lowerString = inputString.lower()
    numA = 0
    numE = 0
    numI = 0
    numO = 0
    numU = 0
    for l in lowerString:
        if l == 'a' or l == 'A':
            numA = numA + 1
        if l == 'e' or l == 'E':
            numE = numE + 1
        if l == 'i' or l == 'I':
            numI = numI + 1
        if l == 'o' or l == 'O':
            numO = numO + 1
        if l == 'u' or l == 'U':
            numU = numU + 1
    nonVowels = len(inputString)  - (numA + numE + numI + numO + numU)
    print("'{}' has {} a's, {} e's, {} i's, {} o's, {} u's, and {} non-vowels".format(inputString, numA, numE, numI, numO, numU, nonVowels))
    
#3
def leastChar(inputString):
    lowerString = inputString.lower()
    leastCharSoFar = inputString[0]
    leastIndex = 0
    currIndex= 0
    for currChar in lowerString:
        if currChar < leastCharSoFar:
            leastCharSoFar = currChar
            leastIndex = currIndex
            # not necessary for full credit. Quits early if 'a' found
            if leastCharSoFar == 'a':
                break           
        currIndex = currIndex + 1
    print("The least char is '{}' and occurs at position {}.".format(inputString[leastIndex], leastIndex))

#4
def generateSequence(startNumber, factor, offset, stopNumber) :
    currNumber = startNumber
    count = 1
    print(currNumber)
    while currNumber != stopNumber:
        if (currNumber%2) == 0:
            currNumber = currNumber // 2
        else:
            currNumber = (currNumber * factor) + offset
        print(currNumber)
        count = count + 1
    print("Length of sequence: ", count)

#####
    
separatorString = 40*'-'

def testQ1():
    print("=============== Testing Q1 ===============")
    print("testing printRanges(4,4):")
    printRanges(4,4)
    print(separatorString)
    print("testing printRanges(9,11):")
    printRanges(11,9)
    print()

def testQ2():
    print("=============== Testing Q2 ===============")
    print("testing printVowelStats('e'):")
    printVowelStats('e')
    print(separatorString)
    print("testing printVowelStats('E'):")
    printVowelStats('E')
    print(separatorString)
    print("testing printVowelStats('uiaOeo'):")
    printVowelStats('uiaoeo')
    print(separatorString)
    print("testing printVowelStats('zswttrs'):")
    printVowelStats('zswttrs')
    print(separatorString)
    print("testing printVowelStats('ooekekekekaal'):")
    printVowelStats('ooekekekekaal')
    print()
    
def testQ3():
    print("=============== Testing Q3 ===============")
    print("testing leastChar('zdb'):")
    leastChar('zdb')
    print(separatorString)
    print("testing leastChar(''bbbAeniQknlqa'):")
    leastChar('bbbAeniQknlqa')
    print(separatorString)
    print("testing leastChar('bbbaeniQknlqa'):")
    leastChar('bbbaeniQknlqa')
    print(separatorString)
    print("testing leastChar('c'):")
    leastChar('c')
    print(separatorString)
    print("testing leastChar('Z'):")
    leastChar('Z')
    print()
    
def testQ4():
    print("=============== Testing Q4 ===============")
    print("testing generateSequence(5,2,2,5):")
    generateSequence(5,2,2,5)
    print("Output should say sequence length is: ",  1)
    print(separatorString)
    print("testing generateSequence(5,3,3,3):")
    generateSequence(5,3,3,3)
    print("Output should say sequence length is: ",  10)
    print(separatorString)
    print("testing generateSequence(5,3,1,1):")
    generateSequence(5,3,1,1)
    print("Output should say sequence length is: ",  6)
    print(separatorString)
    print("testing generateSequence(18,2,2,1):")
    generateSequence(18,2,2,1)
    print("Output should say sequence length is: ", 12)
    print(separatorString)
    print("testing generateSequence(27,3,1,1):")
    generateSequence(27,3,1,1)
    print("Output should say sequence length is: ", 112) 
