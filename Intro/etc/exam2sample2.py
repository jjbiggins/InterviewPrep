def q1(L):                                                                                                
    n = len(L)                                                                                            
    count = 0                                                                                             
    for i in L:                                                                                           
        if i == max(L) or i < 0:                                                                        
           count = count + 1                                                                              
    return count


def q1faster(L):                                                                                                
    n = len(L)                                                                                            
    count = 0
    maxL = max(L)
    for i in L:                                                                                           
        if i == maxL or i < 0:                                                                        
           count = count + 1                                                                              
    return count

import time
def timeq1(n):
    l = list(range(n))
    start = time.time()
    q1(l)
    end = time.time()
    return end-start

def timeq1faster(n):
    l = list(range(n))
    start = time.time()
    q1faster(l)
    end = time.time()
    return end-start

def q2a():
    return len([ c for c in 'computer science' if c not in 'aeiou' ]) 

def q2b():
    return [ ('$'+ str(i) + '.99') for i in range(1,5)]
