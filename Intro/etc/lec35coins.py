import random
import math

def stdDev(values):
    mean = float(sum(values))/len(values)
    diffsum = 0.0
    for item in values:
        diff = item - mean
        diffsum = diffsum + diff*diff
    return math.sqrt(diffsum/len(values))

# simulate flipping a coin numFlips times.
# return tuple (number of heads, number of tails)
#
def doNCoinFlips(numFlips):
    numHeads = 0
    flipNum = 0
    while flipNum < numFlips:
        value = random.randint(1,2)
        if value == 1:
            numHeads = numHeads + 1
        flipNum = flipNum + 1
    return (numHeads, numFlips-numHeads)

# Do numTrials coin flip simulations with numCoins each time.
# For each trial compute ratio of number of heads to number of trials.
# Compute average and standard deviation of the ratios over all trials.
# Print summary and
# return tuple (average heads/tails ratio, standard devation of ratio)
# 
def doCoinFlipTrials(numTrials, numCoins):
    headTailRatios = []
    headTailDiffs = []
    for trial in range(numTrials):
        nHeads, nTails = doNCoinFlips(numCoins)
        #print("Trial #{}: numHeads = {}, numTails = {}".format(trial, nHeads, nTails))
        # NOTE: This code *can* crash - it's unlikely but nTails can, of course, be 0 
        headTailRatios.append(float(nHeads)/nTails)
        
    ratiosAvg = sum(headTailRatios)/len(headTailRatios)
    ratiosStdDev = stdDev(headTailRatios)
    
    print("# of flips = {}: avg head/tail ratio: {} (SD: {})".format(numCoins, ratiosAvg, ratiosStdDev))
    return (numCoins, ratiosAvg, ratiosStdDev)
    
# Execute doCoinFlipTrials for different numbers of coins (and given number of trials),
# starting with minCoins and increasing by factor until number exceeds maxCoins.
# Return list of results returned by the calls to doCoinFlipTrials.
# Thus, results will be of form [(minCoins, ..ratio.., ...std...), (factor*minCoins, ..ratio.., ...std..), ...]
#
def doCoinFlipExperiment(minCoins, maxCoins, factor, numTrials=20):
    numCoins = minCoins
    results = []
    while numCoins <= maxCoins:
        results.append(doCoinFlipTrials(numTrials, numCoins ))
        numCoins = numCoins * factor
    return results

# Uncomment section below if you have pylab
'''
import pylab

# results = doCoinFlipExperiment(16, 2**20, 2)
# plotResults(results)
# pylab.show()
#
#
# Create figure with two subplots, one showing avg. head/tail ratios for different numbers of
# coin flips, the other showing standard deviation of head/tail ratios.
#
def plotResults(results):
    numFlips, ratios, ratioSDs = tuple(zip(*results))

    pylab.figure(1)
    pylab.clf()
    pylab.subplot(121)
    pylab.title("Head/tail ratios")
    pylab.xlabel("Number of flips")
    pylab.ylabel("Average head/tail ratio")
    pylab.semilogx()
    pylab.plot(numFlips, ratios, 'ro-') 
    
    pylab.subplot(122)
    pylab.title("Std dev. of h/t ratios")
    pylab.xlabel("Number of flips")
    pylab.ylabel("Standard deviation")
    pylab.semilogx()
    pylab.plot(numFlips, ratioSDs, 'ro-')
    
'''
    
