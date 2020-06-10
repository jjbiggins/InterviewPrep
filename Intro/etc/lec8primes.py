import math

def numIsPrime(n):
    isPrime = True
    potentialDivisor = 2
    while potentialDivisor < n:
        if (n % potentialDivisor) == 0:
            isPrime = False
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

# alternate version of numIsPrime.
# Tests fewer potential divisors:
# - only tests up through sqrt(n)
# - returns when divisor is found rather than continuing to check additional potential divisors
def numIsPrimeV2(n):
    potentialDivisor = 2
    while potentialDivisor <= math.sqrt(n):
        print("testing divisor: ", potentialDivisor)
        if (n % potentialDivisor) == 0:
            return False
        potentialDivisor = potentialDivisor + 1
    return True
