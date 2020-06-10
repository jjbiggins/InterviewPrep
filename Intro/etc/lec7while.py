# demonstrate general pattern for iterating through characters
# of a string using while.
# ([] operator is presented in Ch 8)
#
def loopChars(inputString):
    currentIndex = 0
    while currentIndex < len(inputString):
        currentChar = inputString[currentIndex]
        #
        # body of loop - typically do some computation
        # using character currentChar
        #
        print(currentChar)
        currentIndex = currentIndex + 1

# demonstrate general pattern for iterating through characters
# of a string using for.  Understand that this and loopChars() are equivalent.
# (for loop is presented in Ch 8)
#
def loopChars2(inputString):
    for currentChar in inputString:
        #
        # body of loop - typically do some computation
        # using character currentChar
        #
        print(currentChar)


# understand that body of while loop never executes!
#
def whileFn():
    output = "Hello!"
    while False:
        print(output)
    print("all done!")


# with "while != 0" not-very-careful testing might lead to conclusion that this
# code works.
# countDownBy3From(3) prints just 3 (and 'all done'),
# countDownBy3From(18) prints 18 15 12 9 6 3 (and 'all done')
# But what positive numbers cause problems?
# Fix with "current >= 0" instead of "current != 0"
#
def countDownBy3From(number):
    current = number
    while current != 0:   
        print(current)
        current = current - 3
    print("all done")


# This does not yet correctly print primes BUT it is a useful stub because it enables
# us to test structure of printFirstNPrimes().  It's very good practice
# to test code early and often. If you write a lot of code before testing,
# it can take much longer to track down errors.
# With this stub, the printed primes will not be correct BUT we'll see that
# 1) candidate generation works, 2) printing works, 3) the loop terminates, etc.
#
# We will develop correct version of numIsPrime on Friday.
def numIsPrime(n):
    isPrime = True
    return isPrime

def printFirstNPrimes(n):
    numPrimesPrinted = 0
    candidate = 2
    while (numPrimesPrinted != n):
        isPrime = numIsPrime(candidate)
        if isPrime:
            print(candidate)
            numPrimesPrinted = numPrimesPrinted + 1
        candidate = candidate + 1

    
        

            
    
