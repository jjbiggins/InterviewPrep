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

# For Lec 19, exercise 3.
# This method works most of the time but (1) is much slower than a good solution,
#  and (2) gives wrong result in a limited number of cases.  E.g. 
# E.g. for inputList == [1, 2, 5] and k == 4, it would yield "pair" 2, 2
# Can you fix this? 
# 
def findKPairSlow1(inputList, k):
    for item1 in inputList:
        for item2 in inputList:
            if (item1 + item2 == k):
                print("Yay! Found a pair ({}, {}) that sum to {}".format(item1,item2, k))
                return (item1, item2)
    print("No, I couldn't find a pair for the given target.")

 








