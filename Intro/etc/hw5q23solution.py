import random

def randChoicesOrig(listOfLists):
    result = []
    for sublist in listOfLists:
        chosenItem = random.choice(sublist)
        result.append(chosenItem)
    return result

def randChoices(listOfLists):
    return [random.choice(sublist) for sublist in listOfLists]

def howManyNumsWithDigit(upperNumber, digit):
    return len([num for num in range(1,upperNumber+1) if str(digit) in str(num)])

def testQ2():
    print("randChoices([]) returned: {}".format(randChoices([])))
    print("randChoices([[1], [2], [3], [0], [-1]]) returned: {}".format(randChoices([[1], [2], [3], [0], [-1]])))
    print("randChoices([[1, 12, 3, 4, 5], [5, -1, 4, 1, 1], [0, -3, 4, 0, 9]]) returned: {}".format(randChoices([[1, 12, 3, 4, 5], [5, -1, 4, 1, 1], [0, -3, 4, 0, 9]])))


def testQ3():
    res = howManyNumsWithDigit(10,9)
    print("howManyNumsWithDigit(10,9) produced: {}. {}".format(res, "CORRECT" if (res==1) else "INCORRECT"))
    res = howManyNumsWithDigit(10,1)
    print("howManyNumsWithDigit(10,1) produced: {}, {}".format(res, "CORRECT" if (res==2) else "INCORRECT"))
    res = howManyNumsWithDigit(30,2)
    print("howManyNumsWithDigit(20,2) produced: {}. {}".format(res, "CORRECT" if (res==12) else "INCORRECT"))
    res = howManyNumsWithDigit(40,2)
    print("howManyNumsWithDigit(40,2) produced: {}. {}".format(res, "CORRECT" if (res==13) else "INCORRECT"))
    res = howManyNumsWithDigit(100,1)
    print("howManyNumsWithDigit(100,1) produced: {}. {}".format(res, "CORRECT" if (res==20) else "INCORRECT"))
    res = howManyNumsWithDigit(100,0)
    print("howManyNumsWithDigit(100,0) produced: {}. {}".format(res, "CORRECT" if (res==10) else "INCORRECT"))
    res = howManyNumsWithDigit(1001,0)
    print("howManyNumsWithDigit(1001,0) produced: {}. {}".format(res, "CORRECT" if (res==182) else "INCORRECT"))
    
