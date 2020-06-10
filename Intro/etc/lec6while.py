# print the first thousand integers, 1...1000, one per line, 
# and then print("All done")
#
def printFirstThousand():
    current = 1
    
    while (current <= 1000):
        print(current)
        current = current + 1
        
    print("All done")

# return sum of first thousand integers: 1...1000
#
def sumOfFirstThousand():
    sum = 0

    current = 1
    while (current <= 1000):
        sum = sum + current
        current = current + 1
        
    return sum

# return the sum of first n integers: 1...n
#
def sumOfFirstN(n):
    sum = 0
    current = 1
    
    while current <= n:
        sum = sum + current
        current = current + 1
        
    return sum

    
