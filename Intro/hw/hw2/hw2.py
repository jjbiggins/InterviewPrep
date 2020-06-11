#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1
# File              : sol.py
# Author            : Joe Biggins <jjbiggins@joebiggins.io>
# Date              : 10.06.2020
# Last Modified Date: 10.06.2020
# Last Modified By  : Joe Biggins <jjbiggins@joebiggins.io>
# Created by jjbiggins  at 6/10/2020
import timeit
import os
from timeit import Timer
import time
def printRanges(high, low):
	arr = list (range (low, high))
	zeroLow = list (range (0, low))
	
	for i in arr:
		print (high)
		print (zeroLow [:] + arr [:-1])
		
		high = arr [-1]
		arr = arr [:-1]
	
	print (low)
	print (zeroLow [:])

def testPrintRanges():
	start_time = time.time ()
	printRanges(1000, 324)
	print ("--- %s seconds ---" % (time.time () - start_time))

def printVowelStats(inputString):
	vowels = ['a', 'e', 'i', 'o', 'u', 'non-vowels']
	final = [each for each in inputString if each in vowels]
	
	vowelsDict = {}.fromkeys (vowels, 0)
	vowelsDict['non-vowels'] = len(inputString) - len (final)
	for i in final:
		vowelsDict [i] += 1
	
	print (vowelsDict)
	
def leastChar(inputString):
	input = sorted(inputString)
	times = 0
	for i in range(len(inputString)):
		if input[i] == input[0]:
			times += 1
		elif input[i].upper() == input[0]:
			times += 1
		else:
			times = times
	print(str(input[0]) + ": " + str(times))
	return

def  generateSequence(startNumber, factor, offset, stopNumber):
	i = startNumber
	count=0
	while i != stopNumber:
		print(i)
		if i % 2 == 0:
			i = i / 2
		else:
			i = (i*factor) + offset
		count+=1
	count+=1
	print(stopNumber)
	print("Length seq: " + str(count))