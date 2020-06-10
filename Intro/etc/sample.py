# This is an example one kind of problem that is very likely to be on the final
# exam.
#
# Given a list of integers, do f1, f2, and f3 always produce equal results?
# If not, provide input values for which results differ.

def f1(listOfNumbers):
    result = 0
    for num in listOfNumbers:
        if ((num%2 == 0) or (num%3 == 0)):
            result = result + 1
    return result

def f2(listOfNumbers):
    result = 0
    for num in listOfNumbers:
        if num%2 == 0:
            result = result + 1
        if num%3 == 0:
            result = result + 1
    return result           

def f3(listOfNumbers):
    result = 0
    i = 1
    while i < len(listOfNumbers):
        num = listOfNumbers[i]
        if num%2 == 0:
            result = result + 1
        if num%3 == 0:
            result = result + 1
        i = i + 1
    return result           
