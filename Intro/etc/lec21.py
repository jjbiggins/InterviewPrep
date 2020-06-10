# if you pass in a tuple, this will crash
def twiceLen(inList):
    inList[0] = -inList[0]
    return 2*len(inList)


def twiceAndThriceN(n):
    return (2*n, 3*n)

zippedStuff = zip([1,2,3], ['a', 'b', 'c'])

zipObj = zip([1, 2, 3], ['uno', 'dos', 'tres'], ['mot', 'hai', 'ba'])

d = {'free': 23, 'you': 50, 'go': 10, 'zoo': 1}

def item1(element):
    return element[1]

tl = [('free', 23), ('you', 50), ('go', 10), ('zoo', 1)]

sorted(tl, key = item1)

sorted(tl, key = lambda item: item[1], reverse = True)

(lambda x,y: x + y)(2,3)

myAdd = lambda x, y: x + y

def generateTimesNFunc(n):
    return lambda x: n*x
