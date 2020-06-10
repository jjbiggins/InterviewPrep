def problem1():
    print (2//5)
    print (not ( (5 > len(range(5))) or ("mot" == "one") ))
    print ("[a, b, c]" + "[d]")
    
def problem2a():
    w = 1
    x = 17
    y = w + 1
    z = [x, y]
    y = y + w
    z[0] = x + 1
    z.append(y)
    print(w, x, y, z)

# you must set values for x, y, z in the interpreter before calling problem2b()
def problem2b():
    if ((y > z) or (z < x)):
        print("EK")
        if (x < 10):
            print("DO")
        elif (z < 10):
            print("TEEN")
        print("CHAAR")
    else:
        if (x < 20):
            print("PAANCH")
        else:
            print("CHAH")
        print("SAAT")
    if ((z-y) > 0):
        print("AATH")

# presumes 1) there are at least two items in the list, 2) all items in the list are unique
# There assumptions aren't in the in the exam document but were written on board at the
# beginning of the exam
# Normally, you should not presume input lists are non-empty (unless explicitly stated in the
# specification.)
def problem3 (numList):
    # First, initialize biggest/secondbiggest/total, using assumption that list
    # contains at least two items.
    if (numList[1] < numList[0]):
        biggest = numList[0];
        secondbiggest = numList[1]
    else:
        biggest = numList[1]
        secondbiggest = numList[0]
    total = numList[0] + numList[1]

    # Go through remainder of list, updating biggest, secondbiggest, total appropriately
    for item in numList[2:]:
        total = total + item
        if (item > biggest):
            secondbiggest = biggest
            biggest = item
        elif (item > secondbiggest):
            secondbiggest = item
    avg = float(total)/len(numList)
    print("biggest: " + str(biggest) + " second: " + str(secondbiggest) + " avg: " + str(avg))
            
# sample input: [["girl", "boy"], [0, 2, 7, 4], [[], 'x']]
def problem4(listOfLists):
    result = []
    for item in listOfLists: 
        result.append(len(item))
    return(result)

def problem4c(listOfLists):
    result = []
    i = 0
    while (i < len(listOfLists)):
        item = listOfLists[i] 
        result.append(len(item))
        i = i+1
    return(result)

# test case: [['a', 1, 2, 3], ['b', 1, 2, 4], ['c', 4, 2, 1]] 
def mostDominantTrait(listOfPeopleLists):
    numHappy = 0
    numHealthy = 0
    numWealthy = 0
    for person in listOfPeopleLists:
        if (person[1] > person[2]):
            if (person[1] > person[3]):
                numHappy = numHappy + 1
            else:
                numWealthy = numWealthy + 1
        else:
            if (person[2] > person[3]):
                numHealthy = numHealthy + 1
            else:
                numWealthy = numWealthy + 1
    if (numHappy > numHealthy):
        if (numHappy > numWealthy):
            print("Happiness is dominant")
        else:
            print("Wealthiness is dominant")
    else:
        if (numHealthy > numWealthy):
            print("Healthiness is dominant")
        else:
            print("Wealthiness is dominant")

