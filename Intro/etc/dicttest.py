def testlist(key, inputlist):
    return (key in inputlist)

def testdict(key, inputdict):
    return (key in inputdict)

def createlist(n):
    return list(range(n))

def createdict(n):
    result = {}
    i = 0
    while (i < n):
        result[i] = i
        i = i + 1
    return result

l1 = createlist(1000000)
d1 = createdict(1000000)

import timeit
# timeit.timeit('testlist(100,l1)',  'from __main__ import l1, d1, testlist, testdict', number = 1000000)
# try 200 and 400. What about 500000?
#also try
# timeit.timeit('testlist(999999,l1)',  'from __main__ import l1, d1, testlist, testdict', number = 1)
# timeit.timeit('testlist(999999,l1)',  'from __main__ import l1, d1, testlist, testdict', number = 10)
# timeit.timeit('testlist(999999,l1)',  'from __main__ import l1, d1, testlist, testdict', number = 100)
# etc.

# Then try
# timeit.timeit('testdict(100,d1)',  'from __main__ import l1, d1, testlist, testdict', number = 1000000)
# try 200, 400, 500000, 999999
