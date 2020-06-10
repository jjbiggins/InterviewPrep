def foo(num):
    return num

def q1ab(n):
    result = 0
    i=n
    for i in range(n):
        for j in range(n):
            result = result + (i * foo(j) * foo(i+j))
    return result


import time
def timeq1ab(n):
    start = time.time()
    q1ab(n)
    end = time.time()
    return end-start

def q1cd(n):                                                                                                          
    result = 1                                                                                                        
    i = 1                                                                                                             
    while i < n:                                                                                                      
        result = result + (2 * i)
        i = i + 1                                                                                                     
    for num in range(n):                                                                                              
        result = result + (num - 10)
    return result

def timeq1cd(n):
    start = time.time()
    q1cd(n)
    end = time.time()
    return end-start


def printAllDirectFlights(g):
    for origin in g:
        for dest in g[origin]:
            print("There is a direct flight from {} to {}.".format(origin, dest))
            
def p2():
    g =  {"ORD" : ["JFK", "LAX", "SFO"],
          "CID" : ["DEN", "ORD"],
          "DEN" : ["CID", "SFO"],
          "JFK" : ["LAX"],
          "LAX" : ["ORD"],
          "SFO" : []}
    printAllDirectFlights(g)
         
def selectionSort(L):
    i = 0
    while i < len(L):
        minIndex = findMinIndex(L, i)
        L[i], L[minIndex] = L[minIndex], L[i]
        i = i + 1

        print(L)

def findMinIndex(L, startIndex):
    minIndex = startIndex
    currIndex = minIndex + 1
    while currIndex < len(L):
        if L[currIndex] < L[minIndex]:
            minIndex = currIndex
        currIndex = currIndex + 1
    return minIndex

def p3():
     selectionSort([3, 99, -2, 17, 5])

class Box:                                                                                                            
    def __init__(self, width, height, depth, maxWeight):                                                              
        self.width = width                                                                                            
        self.height = height                                                                                          
        self.depth = depth                                                                                            
        self.maxWeight = maxWeight                                                                                    
                                                                                                                      
        self.objectsInside = []                                                                                       
        self.currentWeightInside = 0                                                                                     
        self.currentNumberOfObjectsInside = 0                                                                                                                                                                                              
                                                                                                                      
    def volume(self):                                                                                                 
        return self.width * self.height * self.depth                                                                  
                                                                                                                      
    def numberOfObjectsInside(self):                                                                                  
        return self.currentNumberOfObjectsInside                                                                      
                                                                                                                      
    def remainingWeightCapacity(self):                                                                                
        return self.maxWeight - self.currentWeightInside                                                              
                                                                                                                      
    # If the box's weight capacity will not be exceeded,                                                              
    #  add given object to the box, updating objectsInside, currentWeightInside and currentNumberOfObjectsInside      
    # Otherwise, print an appropriate message.                                                                        
    #                                                                                                                 
    def addObject(self, object, objectWeight):
        if objectWeight > self.remainingWeightCapacity():
            print("There's not enough remaining capacity")
            return
        self.objectsInside.append(object)
        self.currentWeightInside = self.currentWeightInside + objectWeight
        self.currentNumberOfObjectsInside = self.currentNumberOfObjectsInside + 1
        return
                                                                                                                      
    # Return False if the size (by volume) of self is larger than that of the other box, False otherwise.             
    #                                                                                                                 
    def isLargerThan(self, otherBox):                                                                                 
        return (self.volume() > otherBox.volume())

def p4():
    box1 = Box(3, 2, 4, 100)
    box2 = Box(2,3,5, 20)
    print(box1.isLargerThan(box2))
    box1.addObject("o1", 90)
    print(box1.numberOfObjectsInside())
    box1.addObject("o2", 9)
    print(box1.numberOfObjectsInside())
    box1.addObject("o3", 5)
    print(box1.numberOfObjectsInside())
    return (box1, box2)
