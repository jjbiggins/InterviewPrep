# to run this file you'll need to download ds4solution.py (will be posted at 5:30pm on 2/15
# when all discussion sections are finished)
from ds4solution import *

# Naive solution! Will be too slow for large file.  We will develop a fast version later.
#
def biggestAnagramSet(filename):
    wordList = getWordList(filename)
    print("Read {} words from {}.".format(len(wordList), filename))
    biggestAnagramList = []
    for word in wordList:
        anagramList = findAnagramsOf(word, wordList)
        if len(anagramList) > len(biggestAnagramList):
            biggestAnagramList = anagramList
    print(biggestAnagramList)
    print("The largest set of anagrams contains {} words.".format(len(biggestAnagramList)))
