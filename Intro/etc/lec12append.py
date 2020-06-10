
def makeList1(n):
    result = []
    for num in range(n):
        result = result + [num*num]
    return(result)

def makeList2(n):
    result = []
    for num in range(n):
        result.append(num*num)
    return(result)

import time

# Try compareTimes(10000)                                                       
#     compareTimes(20000)                                                       
#     compareTimes(40000)                                                       
#     compareTimes(80000)                                                       
#    
def compareTimes(n):
    time1 = time.time()
    result = makeList1(n)
    time2 = time.time()

    time3 = time.time()
    result = makeList2(n)
    time4 = time.time()

    print("for n = {}: makeList1 time = {:.4f}, makeList2 time = {:.4f}".format(n, time2-time1, time4-time3)) 


