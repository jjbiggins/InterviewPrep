import random

def mixupBad(L):
    newL = L[:]
    length = len(L)
    for i in range(length):
        
        newIndex = random.randint(0,  length-1)
        newL[newIndex], newL[i] = newL[i], newL[newIndex]
    return(newL)

def mixup(L):
    newL = L[:]
    length = len(L)
    for i in range(length):
        
        newIndex = random.randint(i,  length-1)
        newL[newIndex], newL[i] = newL[i], newL[newIndex]
    return(newL)

# this can be used to test mixup. E.g. testMixup(1000000, mixupBad) or testMixup(1000000, mixup)
# Calls mixup n times on list [1,2,3] 
# and tallies the number of times each of six possible permutations was generated
# What do you expect? What do you actually get?
def testMixup(n, fn=mixupBad):
    md = {(0,1,2): 0, (0,2,1): 0, (1,2,0): 0, (1, 0, 2):0, (2,0,1):0, (2, 1, 0):0}
    ml = [0,1,2]
    for i in range(n):
        resultAsTupleKey = tuple(fn(ml))
        md[resultAsTupleKey] = md[resultAsTupleKey] + 1
    print(md)

