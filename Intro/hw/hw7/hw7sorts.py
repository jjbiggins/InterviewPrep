def selectionSort(L):
	i = 0
	# invariant: L[0:i] sorted and in final position
	while i < len (L):
		minIndex = findMinIndex (L, i)
		L [i], L [minIndex] = L [minIndex], L [i]
		# now L[0:i+1] sorted an in final position.
		i = i + 1
	# L[0:i] sorted/in final position,and "loop invariant" (loop entry point assumption) holds again
	
	## uncomment this if you want to see progress (don't do for large L though!)
	# print("sorted and in final pos:", L[0:i], "unsorted:", L[i:])


# return index of min item in L[startIndex:]
# assumes startIndex < len(L)
#
def findMinIndex(L, startIndex):
	minIndex = startIndex
	currIndex = minIndex + 1
	while currIndex < len (L):
		if L [currIndex] < L [minIndex]:
			minIndex = currIndex
		currIndex = currIndex + 1
	return minIndex


def insertionSort(L):
	i = 1
	
	# invariant: L[0:i] is sorted
	while i < len (L):
		itemToMove = L [i]
		# find where itemToMove should go, shifting larger items right one slot along the way
		j = i - 1
		while ((j >= 0) and (itemToMove < L [j])):
			L [j + 1] = L [j]
			j = j - 1
		
		# found the spot - put itemToMove there
		L [j + 1] = itemToMove
		
		# now L[0:i+1] is sorted (though items not necessarily in final position)
		i = i + 1
	# L[0:i] sorted and "loop invariant" (loop entry point assumption) holds again
	
	# uncomment this if you want to see progress (don't do for large L though!)
	# print("sorted:", L[0:i], "unsorted:", L[i:])
	
	return


# Recursive version of merge sort.
# (It's much easier for most people to correctly implement mergesort recursively.)
# Note: this version modifies L itself, like the other sorts.
#
def mergeSort(L):
	if (len (L) < 2):
		return
	else:
		# 1. divide list into (almost) equal halves
		middleIndex = len (L) // 2
		left = L [:middleIndex]
		right = L [middleIndex:]
		
		# 2. recursively sort left and right parts
		mergeSort (left)
		mergeSort (right)
		
		# 3. merge sorted left/right parts
		mergedL = merge (left, right)
		
		# mergedL is now sorted but we need to do one more thing (related to Note above)
		# this copies the contents of margedL into L
		L [:] = mergedL [:]
		return


# Merge function used by both the recursive and non-recursive merge sorts.
def merge(L1, L2):
	mergedL = []
	iL1 = 0
	iL2 = 0
	
	while iL1 != len (L1) and iL2 != len (L2):
		if L1 [iL1] <= L2 [iL2]:
			mergedL.append (L1 [iL1])
			iL1 = iL1 + 1
		else:
			mergedL.append (L2 [iL2])
			iL2 = iL2 + 1
	
	# At this point, we've used up all the items from one of the lists.
	# Use list "extend" method to add all the remaining items to mergedL
	mergedL.extend (L1 [iL1:])
	mergedL.extend (L2 [iL2:])
	
	return mergedL


def builtinSort(L):
	L.sort ()


##########

import random


# return a new list with the same elements as input L but randomly rearranged
def mixup(L):
	newL = L [:]
	length = len (L)
	for i in range (length):
		# be careful: the commented-out 'newIndex = ...' line seems reasonable but is WRONG
		# (but close enough that you might not realize it. see, e.g. http://www.codinghorror.com/blog/2007/12/the-danger-of-naivete.html )
		# WRONG:  newIndex = random.randint(0,  length-1)
		#
		newIndex = random.randint (i, length - 1)
		newL [newIndex], newL [i] = newL [i], newL [newIndex]
	return (newL)


##########

import time


def timeSort(sortfn, L):
	t1 = time.time ()
	sortfn (L)
	t2 = time.time ()
	return (t2 - t1)


# try, e.g.,
# l = mixup(list(range(4000)))
# timeAllSorts(l)
def timeAllSorts(L):
	Lcopy = L [:]
	sTime = timeSort (selectionSort, Lcopy)
	Lcopy = L [:]
	iTime = timeSort (insertionSort, Lcopy)
	Lcopy = L [:]
	mTime = timeSort (mergeSort, Lcopy)
	Lcopy = L [:]
	biTime = timeSort (builtinSort, Lcopy)
	
	print ("{}\t sel: {:.2f}\t ins: {:.2f}\t merge: {:.2f}\t builtin: {:.2f}".format (len (L), sTime, iTime, mTime,
	                                                                                  biTime))
