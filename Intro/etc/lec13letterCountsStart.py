
# Note: this code will crash until letterCounts, otherCharsCount have useful values
#
def printLetterCounts(inputString, letters):

    # 1. create a list, letterCounts, containing a 0 for each letter in letters
    
    # 2. go through characters of string incrementing appropriate letterCounts item if char in letters
    
    # at this point, values in letterCounts should contain correct counts of
    #     of number of times chars in letters appear in inpuString
    #     E.g. for printLetterCounts("this is a sentence", "aze")
    #             letterCounts should be [1, 0, 3]
    # 3. compute (and store as otherChars Count) number of characters in inputString *not* in letters 

    # 4. print results
    print("'{}' has:".format(inputString))
    for l in letters:
        print("\t{} '{}'s".format(letterCounts[letters.index(l)], l))
    print("\tand {} other characters".format(otherCharsCount))
    
