# CS 1210, Spring 2017.
# Discussion section 4, Feb. 14 and 15

# DISCUSSION SECTION WORK:
#
# 1. STUDENTS: download this file, ds4.py, and wordsMany.txt, from
#     http://www.cs.uiowa.edu/~cremer/courses/cs1210/etc/ds4/
#     Save both in the same folder.
#
# 2. TA (aloud) and STUDENTS:  Read the comments down to definition of anagramInfo
#     function. Discuss any questions about what the functions are supposed to do.
#    
# 3. TA demontstrate running anagramInfo("wordsMany.txt") on this unchanged file, to
#         see that it behaves reasonablyeven though the anagram-testing functions aren't yet
#         complete.  STUDENTS should do the same on their computers.
#         Try words and "fake words" (that are unlikely to be in word list) and also Enter/Return.
#
# 4. STUDENTS: Implement areAnagrams, and test it directly.
#         E.g. test via areAnagrams("cat", "act"), areAnagrams("bull", "bulb"), etc.
#
#     BIG HINT (TA DISCUSS THIS HINT IF HELPFUL):
#            How can we test if two words are anagrams?
#                       Type to a Python shell:  sorted("cat") and then sorted("act")
#                        From what you see, you should get an idea of how to
#                        implement areAnagrams very easily.
#   
# 5. STUDENTS: Implement findAnagramsOf and test it.
#     There is a hint in the stub below.
#
# 6. Finally, try anagramInfo("wordsMany.txt") again.
#         Try on whatever words you want. Some suggestions: art, stop, spear, least
#
#     SUBMIT THIS WHOLE FILE ON ICON.
#

#################  

#
# Two words are anagrams of each other if it is possible to rearrange
# the letters to produce the other.
# For example, "rat" and "art" and "tar" are anagrams of each other,
# as are "ropes" and "prose"
#
# Note: it is not enough for the two words just to have the same letters.
# E.g., "bull" and "bulb" are *not* anagrams.  They both contain b, u, and l but
# the bull cannot be rearranged to spell bulb.
#
# Your job is to complete two simple functions:
#
# areAnagrams(word1, word2): returns True if word1 and word2 are anagrams, False otherwise
#
# findAnagramsOf(word1, wordList): returns a list of all words in wordList
#                                                         that are anagrams of word1 (a word is an anagram of itself)
#                                                         so *if* word1 is in wordList, it should be included in the result
#
# Working "stubs" for these are at the bottom of this file.

#
# Two other functions, already complete, are provided for you.
#
#
# anagramInfo(filename): provides an interactive loop for querying about anagrams.
#                                       See details below.
#
# getWordList(filename): given the name of a file of words, return a list containing all the words.
#

#
#. Given the filename of a file of words, this function
#
#  1. first reads all of the words of the file and stores them in a list.
#  2. prints the number of words read
#  3. enters an interactive loop that repeatedly
#      requests the user to type in a word.
#      - If the user types in a word that is in the word list,
#           the function will print a list of the anagrams of that word.
#      - if the user types a word that is not in the word list, a suitable
#        message is printed before requesting input from the user again.
#      - if the user presses only Enter/Return, the loop terminates and the
#        function returns.
#
# (DO NOT MODIFY THIS!)
#
def anagramInfo(filename):

    wordList = getWordList(filename)
    print("Read {} words from file '{}'.".format(len(wordList), filename))
    print("Now you can ask for the anagrams of any word you like.")
    print("(hit Return/Enter when you want to quit)")
    print()
    query = input("What word do you want to know about? ")
    while query != '':
        if query in wordList:
            anagramList = findAnagramsOf(query, wordList)
            print(anagramList)
        else:
            print("'{}' is not in the word list. Please try again.".format(query))
        #
        query = input("What word do you want to know about? ")

    print("Goodbye!")

#
#  given the name of a file of words, return a list containing all the words
#  (DO NOT MODIFY!)
#
def getWordList(filename):
    result = []
    fileStream = open(filename, 'r')
    for line in fileStream:
        word = line.strip()
        result.append(word)
    return result

# return True if word1 and word2 are anagrams, False otherwise
#
def areAnagrams(word1, word2):
    return sorted(word1) == sorted(word2)

#
#  returns a list of all words in wordList that are anagrams of word1
#  Note: a word is an anagram of itself so if word1 is in wordList,
#    it should be included in the result
#

def findAnagramsOf(word1, wordList):
    result = []
    for word2 in wordList:
        if areAnagrams(word1, word2):
            result.append(word2)
    return result







        

            
