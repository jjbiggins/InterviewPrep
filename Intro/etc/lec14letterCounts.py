
#
# printLettersCounts prints the number of occurrences in inputString
# of each letter in letters.
# For example, printLePerCounts("This is a sentence containing a variety of letters", "aeiouy")
# yields:
#
#  'This is a sentence containing a variety of letters' has:
#       4 'a's
#       6 'e's
#       5 'i's
#       2 'o's
#       0 'u's
#       1 'y's
#       and 32 other characters
#
def printLetterCounts(inputString, letters):

    # 1. create a list, letterCounts, containing a 0 for each letter in letters
    letterCounts = len(letters) * [0]
    
    # 2. go through characters of string incrementing appropriate letterCounts item if char in letters - l
    for char in inputString:
        if char in letters:
            charPositionInLetters = letters.index(char)
            letterCounts[charPositionInLetters] = letterCounts[charPositionInLetters] + 1
    
    # at this point, values in letterCounts should contain correct counts of
    #     of number of times chars in letters appear in inpuString
    #     E.g. for printLetterCounts('this is a sentence', 'aze')
    #             letterCounts should be [1, 0, 3]
    # 3. compute (and store as otherChars Count) number of characters in inputString *not* in letters 
    otherCharsCount = len(inputString) - sum(letterCounts)
    
    # 4. print results
    print("'{}' has:".format(inputString))
    for l in letters:
        print("\t{} '{}'s".format(letterCounts[letters.index(l)], l))
    print("\tand {} other characters".format(otherCharsCount))
