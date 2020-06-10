def greatestDifference(inputList):
    minItem = min(inputList)
    maxItem = max(inputList)
    print("{} and {} have the greatest difference: {}".format(minItem, maxItem, maxItem - minItem))

def smallestDifference(inputList):
    sortedList = sorted(inputList)
    minDiffSoFar = sortedList[1] - sortedList[0]
    minIndex = 0
    for index in range(len(sortedList)-1):
        newDiff =  sortedList[index+1] - sortedList[index]
        if newDiff < minDiffSoFar:
            minDiffSoFar = newDiff
            minIndex = index
    print("{} and {} have the smallest difference: {}".format(sortedList[minIndex], sortedList[minIndex+1], minDiffSoFar))

# This method is not quite correct since it allows same item to be used twice:
# E.g. for inputList == [1, 2, 5] and k == 4, it would yield "pair" 2, 2
def findKPairSlow1(inputList, k):
    for item1 in inputList:
        for item2 in inputList:
            if (item1 + item2 == k):
                print("Yay! Found a pair ({}, {}) that sum to {}".format(item1,item2, k))
                return (item1, item2)
    print("No, I couldn't find a pair for the given target.")

# A correct slow method.  Does not allow same item to be used twice (unless the number
# appears more than once in the input list).
# Thus, fails on input: [1, 2, 5], 4
#   and succeeds on : [1, 2, 5, 2], 4
#
def findKPairSlow(inputList, k):
    for index1 in range(len(inputList)):
        item1 = inputList[index1]
        for index2 in range(index1+1, len(inputList)):
            item2 = inputList[index2]
            if (item1 + item2 == k):
                print("Yay! Found a pair ({}, {}) at indices {} and {} that sum to {}".format(item1,item2, index1, index2 , k))
                return (item1, item2)
    print("No, I couldn't find a pair for the given target.")

# Like findKPairSlow1, this version is not *quite* correct since it allows same item
# to be used twice even if it appears only once it list. 
# This can be fixed  without changing speed but providing this version 
# first since it clearly conveys the basic idea.
# (see findKPairFastCorrectReturn if interested in fully correct version)
# 
def findKPairFast(inputList, k):
    mydict = {}
    for item in inputList:
        mydict[item] = True
        
    for item in inputList:
        if (k-item) in mydict:
              print("Yay! Found a pair ({:d}, {:d}) that sum to {:d}".format(item,k-item, k))
              return
    print("No, I couldn't find a pair for the given target.")

# same as findKPairFast but provides location of pair in original list
#
def findKPairFastPlus(inputList, k):
    mydict = {}
    for index in range(len(inputList)):
        item = inputList[index]
        mydict[item] = index

    for index in range(len(inputList)):
        item = inputList[index]
        if (k-item) in mydict:
              print("Yay! Found a pair ({:d}, {:d}) at indices {} and {} that sum to {:d}".format(item,k-item, index, mydict[k-item], k))
              return
    print("No, I couldn't find a pair for the given target.")

# If dictionaries not allowed/available BUT we know that numbers in
# inputList are in a limited range, we can still solve the problem very quickly.
# Basically, use a big list instead as a pseudo-dictionary.
#
# Note: this part version assumes numbers are >= 0 and <= 9999
# but that could easily be changed (just change the 10000 on the first line)
#
# Like with other versions, is not fully correct since allows same number to be
# used twice even if only appears once in list.  This could again be easily fixed.
#
def findKPairFastLimited(inputList, k):
    bigList = [False] * 10000
    for item in inputList:
        bigList[item] = True

    for item in inputList:
        if bigList[k-item] == True:
            print("Yay! Found a pair ({:d}, {:d}) that sum to {:d}".format(item,k-item, k))
            return
    print("No, I couldn't find a pair for the given target.")

# Fully correct fast version that returns pairs rather than printing.
# 
# does not allow same item to be used twice (but does allow same
# *number* to be used twice if appears more than once in the list)
# 
def findKPairFastCorrectReturn(inputList, k):
    mydict = {}
    for index in range(len(inputList)):
        item = inputList[index]
        if item in mydict:
            mydict[item].append(index)
        else:
            mydict[item] = [index]
            
    for index in range(len(inputList)):
        item = inputList[index]
        if (k-item) in mydict:
            if k != 2*item:
                # two different numbers
                return (index, mydict[k-item][0])
            elif len(mydict[item]) > 1:
                # can use same number twice *if* it appears in input list more than once
                return (mydict[item][0], mydict[item][1])
    return False



import random
def mixup(L):
    newL = L[:]
    length = len(L)
    for i in range(length):
        newIndex = random.randint(i,length-1)
        newL[newIndex], newL[i] = newL[i], newL[newIndex]
    return(newL)

def randomIntList(n, minInt, maxInt):
    result = []
    for i in range(n):
        newInt = random.randint(minInt, maxInt)
        result.append(newInt)
    return(result)

# create a list of n integers, each randomly selected from range -maxMag to maxMag
# Then for each number 0...999 test if the list contains a pair that sums to that number.
#
def testFindKPair(n, maxMag):
    global l
    global results
    results = []
    l = randomIntList(n, -maxMag, maxMag)
    numYes = 0
    numNo = 0
    for i in range(1000):
        result = findKPairFastCorrectReturn(l, i)
        if not result:
            numNo = numNo + 1
        else:
            results.append([i, l[result[0]], l[result[1]]])
            numYes = numYes + 1
    print("num yes: {}, num no: {}".format(numYes, numNo))
    return results

# First test on small lists both when pairs exist and don't                     
#                                                                               
# Then test on                                                                  
# l = list(range(10000))                                                        
# findKPairSlow(l, 9999)                                                        
# findKPairSlow(l,-1)                                                        
# Then try similar queries on these:                                      
# l = list(range(20000))                                                        
# l = list(range(40000))

# Then try findKPairFast. E.g.
# l = list(range(1000000))
# findKPairFast(l,-1)
# You should see that the fast version is very fast for large lists both when
# pair exists and doesn't exist.

# For insight on Question 6 from lecture slides, try these:

#  l = randomIntList(10000, -1000000, 1000000)
# findKPairFastPlus(l, 14)
# findKPairFastPlus(l, 15)

# res = testFindKPair(10, 1000000)
# res = testFindKPair(1000, 1000000)
# res = testFindKPair(10000, 1000000)








