
# Don't use variable names like these. Makes bugs harder to find.
def farthestFrom1(goalVal, listOfNumbers):
    g = 0
    h = 0
    for i in listOfNumbers:
        j = abs(i - goalVal)
        if j > g:
            g = i
        
    return g

# A common answer on exam 1 but not correct.
def farthestFrom2(goalVal, listOfNumbers):
    far = 0
    for val in listOfNumbers:
        distance = abs(val - goalVal)
        if (distance > far):
            far = distance
    return far

# Also fairly common. Close but still not correct!
# Make sure you know why/when this fails.
def farthestFrom3(goalVal, listOfNumbers):
    maxDist = 0
    farthestVal = 0
    for val in listOfNumbers:
        distance = abs(val - goalVal)
        if (distance > maxDist):
            maxDist = distance
            farthestVal = val
    return farthestVal

# Question 6
#
# farthestFrom(9, [11, 24, 2, 5])
# farthestFrom(4, [6, 1])
# farthestFrom(9, [9])
#
def farthestFrom(goalValue, listOfNumbers):
    farthestSoFar = listOfNumbers[0]
    for item in listOfNumbers[1:]:
        if (abs(item-goalValue) > abs(farthestSoFar-goalValue)):
            farthestSoFar = item
    return farthestSoFar
