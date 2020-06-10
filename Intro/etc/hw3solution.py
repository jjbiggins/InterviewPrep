# CS1210 Spring 2017 HW3 solutions
#
import math

# Q1
def printStringStats(inputString):
    lowerString = inputString
    first = lowerString[0]
    second = None
    third = None

    # Just go through string once, updating first, second, third when appropriate
    for char in lowerString:
        if (first == None) or (char > first):
            third = second
            second = first
            first = char
        elif (char != first) and ((second == None) or (char > second)):
            third = second
            second = char
        elif (char != first) and (char != second) and ((third == None) or (char > third)):
            third = char
            
    # Traverse the string once more (this work could easily be done in the loop above,
    # but I've made it a separate loop because some find it easier to understand.)
    # to find the character that occurs most often.
    maxNumOccurrences = 0
    for charToCount in lowerString:
        charCount = 0
        for char in lowerString:
            if charToCount == char:
                charCount = charCount + 1
        if charCount > maxNumOccurrences:
            maxNumOccurrences = charCount
            mostCommonLetter = charToCount

    print("In '{}', the largest letter is '{}', the third largest letter is '{}',\n and the most common letter is '{}', occurring {} times".format(inputString, first, third, mostCommonLetter, maxNumOccurrences))

# assumes n >= 2
def numIsPrime(n):
    potentialDivisor = 2
    while potentialDivisor <= math.sqrt(n):
        if (n % potentialDivisor) == 0:
            return False
        potentialDivisor = potentialDivisor + 1
    return True

# Q2
def primeDivisorsOf(num):
    result = []
    for i in range(2,num+1):
        if (num%i == 0) and (numIsPrime(i)):
            result.append(i)
    return result

# Q3

def innerMin(listOfLists):
    minItem = None
    minList = None

    for subList in listOfLists:
        for item in subList:
            if (minItem == None) or (item < minItem):
                minItem = item
                minList = subList
    if minItem == None:
        print("Input {} has no minimum.".format(listOfLists))
    else: 
        print("In {} the min item is {} and is found in sublist {}".format(listOfLists, minItem, minList))


# Q4

def testQ1():
    printStringStats('bbbcbyyyzabyyccc')
    printStringStats('aaczzcqzqqqzqc')
    printStringStats("aaaaba")
    printStringStats("cbacc")
    printStringStats("cbac")    
    printStringStats('ab')
    printStringStats('zx')

    
def testQ2():
    print(primeDivisorsOf(4))
    print(primeDivisorsOf(23))
    print(primeDivisorsOf(24))
    print(primeDivisorsOf(36))
    print(primeDivisorsOf(1024*1024+1))
    print(primeDivisorsOf(5003*5003+1))
    print(primeDivisorsOf(1))
    
def testQ3():
    innerMin([[3, 7], [9, 4, 6]])
    innerMin([[4, 0, 1], [2, 3, -1], [5], [6]])
    innerMin([[1000000000000000000]])
    innerMin([[3], [], [1, -5, -2]])
    innerMin([[-3, -2, -100], []])
    innerMin([[], [], [1000000000000000000], []])
    innerMin([])
    innerMin([[],[],[]])



    
