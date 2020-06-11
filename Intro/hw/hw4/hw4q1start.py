#
# CS1210 Spring 2017 HW4 Q1 

# Follow steps 1 through 3 to complete an interactive program that prints information about
# "neighbor" words in a file of words.
#
# Here is a sample session (NOTE: try your code on small file first!)
#
#  >>> wordNeighborInfo('words5000.txt')
#  There are 3143 'lonely' words:
#  The average number of neighbors is 1.63.
#  'hear' has the most neighbors - 19 of them: year, head, wear, near, head, fear, heat, bear, fear, tear, tear, gear, bear, dear, rear, heat near, near, heal, 
#
#  Next, you can query about the neighbors of any word you like.
#  (hit Return/Enter when you want to quit)
#
#  What word do you want to know about? cat
#  'cat' has the 14 neighbors: can, car, cut, eat, cut, fat, hat, cap, fat, can, rat, bat, cab, pat 
#  What word do you want to know about? moozik
#  'moozik' is not in the word list.
#  What word do you want to know about? moon
#  'moon' has the 4 neighbors: soon, mood, soon, noon
#  What word do you want to know about? 
#  Goodbye!
#  >>> 
#

#
# STEP 1. Finish function areNeighbors(word1, word2) 
#
# return True if word1 and word2 
# 1) are the same length 
# and
# 2) differ from each other at exactly one position
# return False otherwise
#
# areNeighbors('cat', 'act') -> False
# areNeighbors('cat', 'scat') -> False
# areNeighbors('cat', 'bat') -> True
# areNeighbors('cart', 'cast') -> True
#
# IMPORTANT NOTE: In the rest of this document, we'll
# call any pair of words, word1 and word2, "neighbors"
# areNeighbors(word1, word2) is True
#
# Test this function thoroughly before going on to others!!
#
def areNeighbors(word1, word2):
	result = False
	# ADD YOUR CODE HERE
	return result


#
# Step 2. Finish function getNeighborList(word1, wordList)
#
# return a list of words from wordList that are "neighbors" (as defined
# by areNeighbors) of word1
#
# For example, getNeighborList('rat', ['cat', 'dog', 'ran', 'sat', 'moon'])
# will return ['cat', 'ran', 'sat']
#   
def getNeighborList(word1, wordList):
	result = []
	# ADD YOUR CODE HERE
	return result


#
#  Step 3. Finish function generateAndSaveAllNeighborLists(wordList):
#
#  returns a list of lists representing all the "neighbor sets" in given file of words
#  Each neighbor set is itself a list [word neighborList], where
#  neighborList is the list of all neighbors of word.
#
#  Thus for word list: ["rat", "dog", "cat", "ran", "sat", "moon", "soon"]
#  this function returns:
#  [['rat', ['cat', 'ran', 'sat']],
#   ['dog', []],
#   ['cat', ['rat', 'sat']],
#   ['ran', ['rat']],
#   ['sat', ['rat', 'cat']],
#   ['moon', ['soon']],
#   ['soon', ['moon']]]
#
#   I.e. 'rat' has three neighbors, 'soon' and 'moon' each the other as their only neighbor.
#   and 'dog' has no neighbors (we'll call it a 'lonely' word).
#
def generateAndSaveAllNeighborLists(wordList):
	neighborData = []
	# ADD YOUR CODE HERE
	return neighborData


# DO NOT MODIFY ANY OF THE CODE BELOW!
#
def getWordList(filename):
	result = []
	fileStream = open (filename, 'r')
	for line in fileStream:
		word = line.strip ()
		if (len (word) >= 1):
			result.append (word)
	return result


# NOTE: this code will crash until your generateAndSaveAllNeighborLists function
# returns a non-empty list
# TODO: Download and follow the instructions in hw4q1start.py to complete an interactive program that prints information about "neighbor" words in a file of words.
#  Do not add any additional functions to the file. Do not change the names of any functions in the file.
#  Do "clean up" the file as you complete the work, eliminating the instruction comments. In the end the file should have only comments that make sense for a finished program.
def wordNeighborInfo(filename):
	wordList = getWordList (filename)
	neighborData = generateAndSaveAllNeighborLists (wordList)
	
	largestNeighborInfo = None
	lonelyWords = []
	
	numberOfNeighborLists = len (neighborData)
	sumAllNeighborListLengths = 0
	
	for neighborInfo in neighborData:
		word = neighborInfo [0]
		neighborList = neighborInfo [1]
		sumAllNeighborListLengths = sumAllNeighborListLengths + len (neighborList)
		
		if len (neighborList) == 0:
			lonelyWords.append (word)
		
		if (largestNeighborInfo == None) or (len (neighborList) > len (largestNeighborInfo [1])):
			largestNeighborInfo = neighborInfo
	
	print ("There are {} 'lonely' words:".format (len (lonelyWords)))
	print ("The average number of neighbors is {:.2f}.".format (sumAllNeighborListLengths / numberOfNeighborLists))
	print (
			"\'{}' has the most neighbors - {} of them: ".format (largestNeighborInfo [0],
			                                                      len (largestNeighborInfo [1])),
			end = '')
	for word in largestNeighborInfo [1] [:-1]:
		print (word, end = ", ")
	print (largestNeighborInfo [1] [-1])
	print ("")
	print ("Next, you can query about the neighbors of any word you like.")
	print ("(hit Return/Enter when you want to quit)")
	print ()
	query = input ("What word do you want to know about? ")
	while query != "":
		neighborList = None
		for neighborSet in neighborData:
			word = neighborSet [0]
			if word == query:
				neighborList = neighborSet [1]
				break
		if neighborList == None:
			print ("\'{}' is not in the word list.".format (query))
		elif len (neighborList) == 0:
			print ("\'{}' has no neighbors.".format (query))
		else:
			print ("\'{}' has the {} neighbors: ".format (query, len (neighborList)), end = '')
			for word in neighborList [:-1]:
				print (word, end = ", ")
			print (neighborList [-1])
		query = input ("What word do you want to know about? ")
	print ('Goodbye!')
	return


def makeChange(amount, coinVal1, coinVal2, coinVal3):
	coins = [coinVal1, coinVal2, coinVal3]
	coinsSorted = sorted (coins)
	myCoins1 = []
	myCoins2 = []
	myCoins3 = []
	
	numBiggestCoin = amount // coinsSorted [-1]
	updatedAmount = amount - (numBiggestCoin * coinsSorted [-1])
	numMedCoin = updatedAmount // coinsSorted [-2]
	updatedAmount = updatedAmount - (numMedCoin * coinsSorted [-2])
	numSmallCoin = updatedAmount // coinsSorted [0]
	updatedAmount = updatedAmount - (numSmallCoin * coinsSorted [0])
	
	myCoins1.append ([coinsSorted [-1]] * numBiggestCoin)
	myCoins2.append ([coinsSorted [1]] * numMedCoin)
	myCoins3.append ([coinsSorted [0]] * numSmallCoin)
	
	myCoins = myCoins1 + myCoins2 + myCoins3
	
	print (myCoins)
	
	return -1


def areSimilar(item1, item2):
	if type (item1) == type (item2):
		if type (item2) != list:
			return True
		elif len (item2) == len (item1):
			return True
		else:
			return False
	else:
		return False

# TODO: Write functions testQ2() and testQ3() that test your Q2 and Q3  functions on a variety of input values.
