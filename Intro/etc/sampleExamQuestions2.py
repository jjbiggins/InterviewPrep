def q1():
    print([1,-6,'h',3][2]*(10//3))
    print([1] + [[3], 'a', [4, 5]])
    print()
    print(((len("[1,2,3,4]") + [1,2,3][1]) > 6) and (not ('E' in 'exam')))
 
# Question 2
                                                                                                                        
def bar(a, b, c):                                                                                                                 
    a = 7 - b                                                                                                                     
    c[0] = a + 15                                                                                                                 
    c = [8]                                                                                                                       
    return [a, b, c]                                                                                                              
                                                                                                                                  
def foo():                                                                                                                        
    a = 4                                                                                                                         
    b = a                                                                                                                         
    c = [1, 2, b]                                                                                                                 
    temp = bar(a, b, c)                                                                                                           
    a = a + 1                                                                                                                     
    return (a, b, c, temp)  

# Q3
def numItemsSmallerThanValue(value, items):                                                                                                                       
    if items == []:                                                                                                                                     
        return 0                                                                                                                                        
    elif items[0] < value:                                                                                                                              
        return 1 + numItemsSmallerThanValue(value, items[1:])                                                                                                                                      
    else:                                                                                                                                               
        return numItemsSmallerThanValue(value, items[1:])

# And one more (not on the pdf)
# Consider this function.
# a) What does it return on .... (particular input)?
# b) In a sentence, what does it do in general?

def program1(thelist, thething):
    if (thelist == []):
        return False
    elif (thelist[0] == thething):
        return True
    else:
        return program1(thelist[1:], thething)
                
