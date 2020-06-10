def findCharOrig(charToFind, stringToSearch):
    for char in stringToSearch:
        if char == charToFind:
            print('found it')
            return        

# Code above prints 'found it' if given charToFind is in stringToSearch
#  but what if we want to know the location (index) of the char in the string?
# (NOTE: yes, there is a built-in Python string method for this, but you should
#  be able to implement this function with a simple loop and comparisons)

# if charToFind is in stringToSearch, return its index
# otherwise return len(stringToSearch)
#
def findChar(charToFind, stringToSearch):
    indexOfCharSought = len(stringToSearch)
    currentIndex = 0
    for char in stringToSearch:
        if char == charToFind:
            indexOfCharSought = currentIndex
            break
        currentIndex = currentIndex + 1
    return indexOfCharSought
