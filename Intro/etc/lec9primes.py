import math
import time

# Try things like compareFinds(1000) - it will likely take several seconds on your computer.
#
# Note: numIsPrime and numIsPrimeFaster use global variable, numTests,
# to count loop interations/divisibility tests.  We've not yet covered global
# variables in class but you don't need to understand global variables to understand the
# numIsPrimeFaster algorithm. numTests is not part of the prime test algorithm; it's simply
# used for operation count/run time analysis comparison.
#
numTests = 0

def numIsPrime(n):
    global numTests
    isPrime = True
    potentialDivisor = 2
    while potentialDivisor < n:
        numTests = numTests + 1
        if (n % potentialDivisor) == 0:
            isPrime = False
        potentialDivisor = potentialDivisor + 1
    return isPrime

def numIsPrimeFaster(n):
    global numTests
    isPrime = True
    potentialDivisor = 2
    while potentialDivisor <= math.sqrt(n):
        numTests = numTests + 1
        if (n % potentialDivisor) == 0:
            isPrime = False
            return False
        potentialDivisor = potentialDivisor + 1
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

def findNthPrime(n):
    numPrimesFound = 0
    candidate = 2
    while (numPrimesFound != n):
        isPrime = numIsPrime(candidate)
        if isPrime:
            savedPrime = candidate
            numPrimesFound = numPrimesFound + 1
        candidate = candidate + 1
    return savedPrime

def findNthPrimeFaster(n):
    numPrimesFound = 0
    candidate = 2
    while (numPrimesFound != n):
        isPrime = numIsPrimeFaster(candidate)
        if isPrime:
            savedPrime = candidate
            numPrimesFound = numPrimesFound + 1
        candidate = candidate + 1
    return savedPrime

def compareFinds(n):
    global numTests

    numTests = 0
    time1 = time.time()
    result = findNthPrime(n)
    time2 = time.time()

    print("findNthPrime({}) required {} tests and {:.4f} seconds to find {}".format(n, numTests, time2-time1, result))
    
    numTests = 0
    time1 = time.time()
    result = findNthPrimeFaster(n)
    time2 = time.time()

    print("findNthPrimeFaster({}) required {} tests and {:.4f} seconds to find {}".format(n, numTests, time2-time1, result))
    

