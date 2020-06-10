def getSmallestAndBiggest(listOfStuff):
    sortedCopyOfList = sorted(listOfStuff)
    return (sortedCopyOfList[0], sortedCopyOfList[-1])

def sortAndGetSmallestAndBiggest(listOfStuff):
    listOfStuff.sort()
    return (listOfStuff[0], listOfStuff[-1])

def countDown(n):
    print("Entering CountDown with n = ", n)

    # base case: time to blast off!
    if n == 0:
        print("Blast Off!")
    else:
        print(n)
        countDown(n-1)

    print("Leaving CD with n = ", n)

def printList(inList):
    if inList == []:
        return
    else:
        print(inList[0])
        printList(inList[1:])

def printListReverse(inList):
    if inList == []:
        return
    else:
        print(inList[-1])
        printListReverse(inList[:-1])
        
def reverseString(inString):
    if inString == '':
        return ''
    elif len(inString) == 1:
        return inString
    else:
        return(reverseString(inString[1:]) + inString[0])

def sumListItems(inList):
    if inList == []:
        return(0)
    else:
        return(inList[0] + sumListItems(inList[1:]))

def isPalindrome(inString):
    if len(inString) < 2:
        return True
    else:
        return((inString[0] == inString[-1]) and (isPalindrome(inString[1:-1])))

def isPalindrome2(inString):
    if len(inString) < 2:
        return True
    if (inString[0] != inString[-1]):
        return False
    return isPalindrome(inString[1:-1])
    
# don't run this on large numbers (i.e. over 40)!
# We'll discuss why later in the semester ...
# 
def fib(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)


