# Question 1
#
def Q1():   
    print( ("123"[1] + "579"[2]) == 11 )
    print( (323 % 5) + (11 // 2 ) ) 
    print( len(range(1,5)) == len("four") )
    print( (not ("H" in "python")) and (len( [[1,2,3]] ) < 3) )
    print( type( [2, 3, 4, [5, [6]]] [3] ) == int )
    print( ([[0],[1],[2]][2]) + [2] )
    print( [5, 7, 9 - 1] + [ "543"[:2]] )


# Question 2
#
def helper2(a):
    a = a * a
    print(a)
    return a

def helper1(a, b, c):
    a = helper2(a) + 1
    b[0] = b[0] + 5
    c.append(a)
    print(a)
    print(b)
    print(c)
    return [a, b, c]

def q2():
    a = 3
    b = [a]
    c = [a + 8]
    helper1Result = helper1(a, b, b)
    print([a, b, c, helper1Result])


# Question 3
#
# q3([1, -3, 3.5, 3, 2, 2.0])
# q3([True, False, 'a'])
# q3([True, False, 'a', 2])
#
def q3(theList):                                                                             
    result1 = 0                                                                              
    result2 = []                                                                             
    for item in theList:                                                                     
        if type(item) == int:                                                               
            result1 = result1 + item                                                         
        else:                                                                               
            result2 = result2 + [item]                                                       
    return [result1, result2] 


# Part c
#
def q3w(theList):                                                                             
    result1 = 0                                                                              
    result2 = []
    index = 0
    while index < len(theList):
        item = theList[index]
        if type(item) == int:                                                               
            result1 = result1 + item                                                         
        else:                                                                               
            result2 = result2 + [item]
        index = index + 1
    return [result1, result2] 


# Question 4
#
def countSublistsAndPositiveItems(listOfLists):                                              
                                                                                             
    numPositiveItems = 0                                                                     
                                                                                             
    numSublists = 0                                                                          
                                                                                             
    for sublist in listOfLists:                                                              
                                                                                             
        numSublists = numSublists + 1                                                                  
                                                                                             
        for item in sublist:                                                             
                                                                                             
            if item > 0:
                numPositiveItems = numPositiveItems + 1
                                                                                                            
    return [numSublists, numPositiveItems]


# Question 5
#
#
def intDiv(numerator, denominator):                                                          
                                                                                             
    if numerator < denominator:                                                              
        return 0                                                                             
                                                                                             
    else:                                                                                    
        return 1 + intDiv(numerator - denominator, denominator)                              
                                                                                             
                                                                                             
def intDivRem(numerator, denominator):                                                       
                                                                                             
    if numerator == 0:                                                                    
        return 0                                                                             
                                                                                             
    elif (numerator - denominator) < 0:                                                      
                                                                                             
        return numerator                                                                            
                                                                                             
    else:                                                                                    
        return intDivRem(numerator - denominator, denominator)                                                                             


# Question 6
#
# farthestFrom(9, [11, 24, 2, 5])
# farthestFrom(4, [6, 1])
# farthestFrom(9, [9])
#
def farthestFrom(goalValue, listOfNumbers):
    farthestSoFar = listOfNumbers[0]
    for item in listOfNumbers[1:]:
        if (abs(item-goalValue) > abs(farthestSoFar-goalValue)):
            farthestSoFar = item
    return farthestSoFar
