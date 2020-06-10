def makeChange(amount, c1, c2, c3):
    if amount < 0:
        return False
    if amount == 0:
        return []
    try1 = makeChange(amount-c1, c1, c2, c3)
    if try1 != False:
        return try1 + [c1]
    try2 = makeChange(amount-c2, c1, c2, c3)
    if try2 != False:
        return try2 + [c2]
    try3 = makeChange(amount-c3, c1, c2, c3)
    if try3 != False:
        return try3 + [c3]
    return False

def areSimilar(item1, item2):
    if type(item1) != type(item2):
        return False
    if type(item1) != list:
        return True
    if len(item1) != len(item2):
        return False
    i = 0
    while (i < len(item1)):
        sItem1 = item1[i]
        sItem2 = item2[i]
        if not areSimilar(sItem1, sItem2):
            return False
        i = i + 1
    return True

def testQ2():
    change = makeChange(53, 2, 3, 5)
    print("makeChange(53, 2, 11, 12) returned {}".format(change))
    change = makeChange(27, 5, 8, 13)
    print("makeChange(27, 5, 8, 13 returned {}".format(change))
    change = makeChange(28, 5, 8, 13)
    print("makeChange(28, 5, 8, 13) returned {}".format(change))
    change = makeChange(28, 8, 13, 5)
    print("makeChange(28, 8, 13, 5) returned {}".format(change))
    change = makeChange(28, 13, 8, 5)
    print("makeChange(28, 13, 8, 5) returned {}".format(change))
    change = makeChange(31, 13, 8, 5)
    print("makeChange(31, 13, 8, 5) returned {}".format(change))
    change = makeChange(30, 13, 7, 5)
    print("makeChange(30, 13, 7, 5) returned {}".format(change))
    change = makeChange(30, 5, 7, 13)
    print("makeChange(30, 5, 7, 13) returned {}".format(change))
    change = makeChange(7, 5, 8, 13)
    print("makeChange(7, 5, 8, 13) returned {}".format(change))
    change = makeChange(100, 3, 7, 5)
    print("makeChange(100, 3, 7, 5) returned {}".format(change))                   
    change = makeChange(0, 1, 2, 3)
    print("makeChange(0, 1, 2, 3) returned {}".format(change))
                        
def testQ3():
    res1 = areSimilar([],[])
    print("For: [], [] result produced: {}.  {}".format(res1, "CORRECT" if (res1==True) else "INCORRECT"))
    res1 = areSimilar([],[3])
    print("For: [], [3] result produced: {}.  {}".format(res1, "CORRECT" if (res1==False) else "INCORRECT"))
    res1 = areSimilar([3, 2.0, 1],[3, 2, 1])
    print("For: [3, 2.0, 1], [3, 2, 1] result produced: {}.  {}".format(res1, "CORRECT" if (res1==False) else "INCORRECT"))
    res1 = areSimilar([3.0],[3])
    print("For: [3.0], [3] result produced: {}.  {}".format(res1, "CORRECT" if (res1==False) else "INCORRECT"))
    res1 = areSimilar([5],[3])
    print("For: [5], [3] result produced: {}.  {}".format(res1, "CORRECT" if (res1==True) else "INCORRECT"))
    res1 = areSimilar([5, [2]],[3, [2.0]])
    print("For: [5, [2]], [3, [2.0]] result produced: {}.  {}".format(res1, "CORRECT" if (res1==False) else "INCORRECT"))
    res1 = areSimilar([5, [2, 3, [3, 2]]], [3, [4, 5, [2, 1.0]]])
    print("For: [5, [2, 3, [3, 2]]], [3, [4, 5, [2, 1.0]]] result produced: {}.  {}".format(res1, "CORRECT" if (res1==False) else "INCORRECT"))
    res1 = areSimilar([1,2,['a','b']],[3,4, [1,2,3]])
    print("For: [1,2,['a','b']], [3,4, [1,2,3]] result produced: {}.  {}".format(res1, "CORRECT" if (res1==False) else "INCORRECT"))
    res1 = areSimilar([1,2,['a', 'b']],[3, 4, ['c', 'hello']])
    print("For: [1,2,['a', 'b']], [3, 4, ['c', 'hello']] result produced: {}.  {}".format(res1, "CORRECT" if (res1==True) else "INCORRECT"))
    res1 = areSimilar([[[[],[2],[],['hi', [0]]]]], [[[[],[-2],[],['bye', [1]]]]])
    print("For: [[[[],[2],[],['hi', [0]]]]], [[[[],[-2],[],['bye', [1]]]]] result produced: {}.  {}".format(res1, "CORRECT" if (res1==True) else "INCORRECT"))
    res1 = areSimilar([[[[],[2],[],['hi', [0]]]]], [[[[],[-2],[],['bye', 0]]]])
    print("For: [[[[],[2],[],['hi', [0]]]]], [[[[],[-2],[],['bye', 0]]]] result produced: {}.  {}".format(res1, "CORRECT" if (res1==False) else "INCORRECT"))
    
