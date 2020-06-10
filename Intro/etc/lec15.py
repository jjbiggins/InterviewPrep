
# given a list, return a "flattened" list containing the same elements
# I.e. [ [[1, 2], 3] , 4, 5, [[[[6]]]], [], 'z' ] --> [1,2,3,4,5,6,'z']
#
# Basically, non-lists are left alone, while any sublists are first themselves flattened and
# then their elements are made part of the result
# E. g. flatten( [ [ 1, 2] , 3 ] ) ->  elements of [1, 2] made part of result along with 3, so [1, 2, 3]
#

def flatten1(aList):
    result = []
    for item in aList:
        if type(item) == list:
            for subListItem in item:
                result.append(subListItem)
        else:
            result.append(item)
    return result

def flatten(aList):
    result = []
    for item in aList:
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Write a recursive function, genSeq(n), that takes a positive
# integer as input and returns a list of numbers as described below.
#
# For 0 through 4, genSeq produces:
# 1 -> [1]
# 2 -> [1, 4, 1]
# 3 -> [1, 4, 1, 9, 1, 4, 1]
# 4 -> [1, 4, 1, 9, 1, 4, 1, 16, 1, 4, 1, 9, 1, 4, 1]
# 5 -> [1, 4, 1, 9, 1, 4, 1, 16, 1, 4, 1, 9, 1, 4, 1, 25, 1, 4, 1, 9, 1, 4, 1, 16, 1, 4, 1, 9, 1, 4, 1]
#

def genSeq(n):
    if n == 1:
        return [1]
    else:
        part = genSeq(n-1)
        return part + [n*n] + part
