# For lots of information on Egyptian fractions see:
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fractions/egyptian.html

# greedily compute Egyptian fraction sum for fraction numerator / denominator
#
# E.g. egypt(761, 1000) yields:  761/1000 = 1/2 + 1/4 + 1/91 + 1/91000
#
# assumption: numerator < denominator
#
def egypt(numerator, denominator):
    
    currentNumerator = numerator
    currentDenominator = denominator
    
    candidateDenominator = 2
    
    print("{}/{} =".format(numerator, denominator), end = '')
    
    firstTime = True
    while currentNumerator > 0:
            # test if 1/candidateDenominator <= currentNumerator / currentDenominator
            # *don't do this by using division! Can cause numerical accuracy problems (see egyptF)
            if (currentDenominator <= (candidateDenominator * currentNumerator)):
                # compute remaining fraction, represented as a numerator and
                # denominator. Again, don't use division!
                currentNumerator = (candidateDenominator * currentNumerator) - currentDenominator
                currentDenominator = (candidateDenominator * currentDenominator)
                if firstTime == True:
                    print(" 1/{}".format(candidateDenominator), end = '')
                    firstTime = False
                else: 
                    print(" + 1/{}".format(candidateDenominator), end = '')
            
            candidateDenominator = candidateDenominator + 1

    print()

# What happens if we use division?
# Try e.g. egyptF(4,5)
#
def egyptF(numerator, denominator):
    
    remainingAmount = numerator / denominator    
    candidateDenominator = 2
    
    print("{}/{} =".format(numerator, denominator), end = '')
    
    firstTime = True
    while remainingAmount > 0:
            # print statement to help you see what's happening when things go wrong ...
            print("\nRemaining amount: ", remainingAmount)
            if (1/candidateDenominator <= remainingAmount):
                remainingAmount = remainingAmount - 1/candidateDenominator
                if firstTime == True:
                    print(" 1/{}".format(candidateDenominator), end = '')
                    firstTime = False
                else: 
                    print(" + 1/{}".format(candidateDenominator), end = '')
            
            candidateDenominator = candidateDenominator + 1

    print()



