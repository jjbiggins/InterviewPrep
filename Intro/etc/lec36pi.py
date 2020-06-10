import random
import math

def stdDev(values):
    mean = float(sum(values))/len(values)
    diffsum = 0.0
    for item in values:
        diff = item - mean
        diffsum = diffsum + diff*diff
    return math.sqrt(diffsum/len(values))
 
def estimatePi(numRandomPts):
    inCircleCount = 0
    pointNumber = 0
    while pointNumber < numRandomPts:
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            inCircleCount = inCircleCount + 1
        pointNumber = pointNumber + 1
        
    return 4 * inCircleCount/float(numRandomPts)

def doPiTrials(numRandomPts, numTrials):
    estimates = []
    for trial in range(numTrials):
        piEst = estimatePi(numRandomPts)
        estimates.append(piEst)
    curEst = sum(estimates)/len(estimates)
    sDev = stdDev(estimates)
    print("Esimate: {}, SD: {}, num random pts {}".format(curEst, sDev, numRandomPts))
    return (curEst, sDev)
    
def findPi(precision, numTrials):
    numRandomPts = 1000
    sDev = precision
    while sDev >= precision/2.0:
        curEst, sDev = doPiTrials(numRandomPts, numTrials)
        numRandomPts = numRandomPts * 2
    return curEst


