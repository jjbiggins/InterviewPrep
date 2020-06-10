def q1(n):
    result = 0
    for i in range(n*n):
        for j in range(n):
            result = result + i*j
    return result

import time
def timeq1(n):
    start = time.time()
    q1(n)
    end = time.time()
    return end-start

def q2a():
    return [ [i, i*i] for i in range(6) ]

def q2b():
    return [ s+s for s in ["mot", "hai", "ba"] if len(s)>2 ]

def printMissingEdges(g):
    for start in g:
        for  possibleEnd in g:
            if possibleEnd not in g[start]:
                print("Edge <{}, {}> is missing.".format(start, possibleEnd))

# A common nice-looking but incorrect solution
# Make sure you understand that "for w not in ..." doesn't work!
'''
def printMissingEdgesTry(g):
    for v in g:
        for w not in g[v]:
            print("Edge <{}, {}> is missing.".format(v, w))
'''                          
                
def testp3b():
    global g
    g = {"RED" : ["GREEN"],
           "GREEN": ["GREEN"],
          "BLUE" : ["RED", "BLUE", "GREEN"]
          } 
    printMissingEdges(g)
    return 
         
class Interval:                                                                                                            
    def __init__(self, low, high):
        if high < low:
            raise ValueError("high value of Interval must be greater than or equal to low value")
        self.low = low                                                                                            
        self.high = high                                                                                                                                                                                             

    # Return True if the given value is contained in the Interval. I.e. if it is greater or                                 
    # equal to the Interval's low value and less than or equal to the intervals high value                                  
    # Otherwise return False.                                                                                               
    def contains(self, value):                                                                                              
        return ((value >= self.low) and (value <= self.high))  

    # Return True if self and otherInterval overlap. I.e. there exists at least one number                                  
    # that is contained in both intervals.  Otherwise return False.                                                         
    def overlaps(self, otherInterval):                                                                                      
        return ((self.low <= otherInterval.high) and (self.high >= otherInterval.low))                                      
      
    def intersection(self, otherInterval):                                                                                  
        if self.overlaps(otherInterval):
            return Interval(max(self.low, otherInterval.low), min(self.high, otherInterval.high))
        else:
            return None

    def union(self, otherInterval):                                                                                  
        if self.overlaps(otherInterval):
            return Interval(min(self.low, otherInterval.low), max(self.high, otherInterval.high))
        else:
            return None

    def __repr__(self):
        return "<interval: {}, {}>".format(self.low, self.high)

def p4():
    i1 = Interval(4, 9.1)
    i2 = Interval(-1, 6)
    print("i1: {}, i2: {}".format(i1, i2))
    print("i1.contains(4.2) returns {}".format(i1.contains(4.2)))
    print("i1.contains(10) returns {}".format(i1.contains(10)))
    print("Result of i1.intersection(i2): {}".format( i1.intersection(i2)))
    print("Result of i2.union(i1): {}".format( i2.union(i1)))

def findMaxIndex(L, endIndex):                                                                                              
    maxIndex = 0                                                                                                            
    currIndex = 0                                                                                                           
    while currIndex <= endIndex:                                                                                             
        if L[currIndex] > L[maxIndex]:                                                                                      
            maxIndex = currIndex                                                                                            
        currIndex = currIndex + 1                                                                                           
    return maxIndex                                                                                                         
                                                                                                                            
def selectionSort2(L):                                                                                                      
    i = len(L)-1
    while i > 0:
        # at this point, L[i+1:] is sorted and all its elements are in final position
        maxIndex = findMaxIndex(L, i)                                                                                  
        L[i], L[maxIndex] = L[maxIndex], L[i]
        # at this point, L[i:] is sorted and all its elements are in final position
        print(i, L)
        i = i - 1                                                                                                           
    return

def computeSomething(L):                                                                                                    
    i = len(L)-1                                                                                                            
    while i > (len(L)-5):                                                                                                  
        maxIndex = findMaxIndex(L, i)                                                                                  
        L[i], L[maxIndex] = L[maxIndex], L[i]                                                                               
        i = i - 1                                                                                                           
    return L[len(L)-4]

def p5():
    selectionSort2([8, 10, 7, 8, 6])
 

