from basicgraph import *
from bfs import *

# Assumption: breadth first search from startNode has already been executed
#
# Extract path from startNode to endNode (by working backwards from endNode),
# returning it as a list e.g. for 'shell'/'spill' the result might be  ['shell', 'spell', 'spill']
# if 'spell' is the parent of 'spill' and 'shell' is the parent of 'spell'
#
def extractWordLadder(startNode, endNode):
     return

# return True if there should be an edge between nodes for word1 and word2 in the
# word graph. Return False otherwise
#
def shouldHaveEdge(word1, word2):
     return

# return word ladder graph for the given file of five-letter words
#
def buildWordGraph(wordsFile = "words5.text"):
     return

# return list of words representing word ladder from startNode to endWord in wordGraph
#
def findWordLadder(startWord, endWord, wordGraph):
     # 1. do graph traversal starting from node for startWord
     # 2. extract word ladder from the graph
     return

# play the word ladder game using the given file of words
#
def wordLadder(wordsFile = "words5.text"):
     # 1. build word graph for the given file of words
     # 2. user interaction loop:
     #     repeatedly ask user to enter two words, and then find and print the word ladder for those words
     return
