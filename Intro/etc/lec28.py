
# search for x in L
def linearSearch(L,x):
    for item in L:
        if item == x:
            return True
    return False

# search for x in L using Python's built-in "in" 
def searchUsingIn(L, x):
    return (True if x in L else False)

# recursive binary search for x in L[startIndex, endIndex]
def binarySearchCore(L, x, startIndex, endIndex):
    if startIndex == endIndex:
        return False
    else:
        midIndex = (startIndex+endIndex)//2
        if x == L[midIndex]:
            return(midIndex)
        elif x < L[midIndex]:
            return(binarySearchCore(L, x, startIndex, midIndex))
        else:
            return(binarySearchCore(L, x, midIndex+1, endIndex))

# recursive binary search for x in L
def binarySearch(L, x):
    return binarySearchCore(L,x,0,len(L))

# search for x in L
def binarySearchIterative(L, x):
    global numIterations
    startIndex = 0
    endIndex = len(L)
    numIterations = 0
    while (startIndex < endIndex):
        numIterations = numIterations + 1
        midIndex = (startIndex+endIndex)//2
        if x == L[midIndex]:
            return(midIndex)
        elif x < L[midIndex]:
            endIndex = midIndex
        else:
            startIndex = midIndex + 1
    return False

import time

# Try, e.g.
# l = list(range(100000000))
# timeSearch(linearSearch, l, 0)
# timeSearch(searchUsingIn, l, 0)
# timeSearch(binarySearch, l, 0)
# timeSearch(binarySearchIterative, l, 0)
# timeSearch(linearSearch, l, -1)
# timeSearch(searchUsingIn, l, -1)
# timeSearch(binarySearch, l, -1)
# timeSearch(binarySearchIterative, l, -1)
#
def timeSearch(searchFn, L, val):
    t1 = time.time()
    searchFn(L, val)
    t2 = time.time()
    return (t2 - t1)


def f(n):
    ans = 0
    for i in range(1000):
        ans = ans + 1
    print('number of additions so far: ', ans)
    for i in range(n):
        ans = ans + 1
    print('number of additions so far:', ans)
    for i in range(n):
        for j in range(n):
            ans = ans + 1
            ans = ans + 1
    print('number of additions so far:', ans)
    return ans




