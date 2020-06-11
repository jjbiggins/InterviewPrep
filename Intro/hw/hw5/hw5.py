#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : hw5.py
# Author            : Joe Biggins <jjbiggins@joebiggins.io>
# Date              : 11.06.2020
# Last Modified Date: 11.06.2020
# Last Modified By  : Joe Biggins <jjbiggins@joebiggins.io>
import sys
import os

from typing import Any
from typing import Optional


def hamAndSpam():
	filestream = open ("SMSSpamCollection.txt", encoding = 'utf-8')
	
	return 0



# Class initialization
class Node (object):
	# Constructor for a Node object
	def __init__(self, char: str):
		# methods that make up a Node object
		self.char = char
		self.children = []
		# Is it the last character of the word.`
		self.word_finished = False
		# How many times this character appeared in the insertition process
		self.counter = 1

class Node:
	def __init__(self) -> None:
		# Note that using a dictionary for children (as in this implementation)
		# would not by default lexicographically sort the children, which is
		# required by the lexicographic sorting mentioned in the next section
		# (Sorting).
		self.children: dict[str, Node] = {}  # mapping from character to Node
		self.value: Optional[Any] = None


def find(node: Node, key: str) -> Optional[Any]:
	"""Find value by key in node."""
	for char in key:
		if char in node.children:
			node = node.children[char]
		else:
			return None
	return node.value


def insert(node: Node, key: str, value: Any) -> None:
	"""Insert key/value pair into node."""
	for char in key:
		if char not in node.children:
			node.children [char] = Node ()
		node = node.children [char]
	node.value = value


if __name__ == "__main__":
	root = Node()
	print(insert (root, "hackathon", root.value))
	insert (root, 'hackathon', root.value)

	print (find (root, 'hac'))
	print (find (root, 'hack'))
	print (find (root, 'hackathon'))
	print (find (root, 'ha'))
	print (find (root, 'hammer'))

import string
import re

# Open the file in read mode
text = open ("SMSSpamCollection.txt", "r")
missed = 0
# Create an empty dictionary
d = dict ()
spam = dict ()
# Loop through each line of the file
for line in text:
	# Remove the leading spaces and newline character
	line = line.strip ()
	pattern = re.compile('([^\s\w]|_)+')
	line = pattern.sub('', line)
	# Convert the characters in line to
	# lowercase to avoid case mismatch
	line = line.lower ()
	
	# Split the line into words
	words = line.split (" ")
	
	# Iterate over each word in line
	
	if words [0] [0] == 'h':
		for word in words [0:]:
			# Check if the word is already in dictionary
			if word in d:
				# Increment count of word by 1
				d [word] = d [word] + 1
			else:
				# Add the word to dictionary with count 1
				d [word] = 1
	elif words [0] [0] == 's':
		for word in words [0:]:
			# Check if the word is already in dictionary
			if word in spam:
				# Increment count of word by 1
				spam [word] = spam [word] + 1
			else:
				# Add the word to dictionary with count 1
				spam [word] = 1
	else:
		missed += 1
# Print the contents of dictionary
for key in list (d.keys ()):
	print (key, ":", d [key])

print ()

for key in list (spam.keys ()):
	print (key, ":", spam [key])

print (len (d))
print (len (spam))
