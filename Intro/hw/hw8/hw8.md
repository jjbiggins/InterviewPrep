CS1210 Homework 8

**Homework 8**\
CS1210 Computer Science 1\
Due Wednesday, April 19, by 9:00am\
10 points\
\

**1.** (6 points) Implement a program to play the Word Ladder game by
completing the functions in [wordLadderStart.py](wordLadderStart.py).
(Note: you\'ll also need these files: [basicgraph.py](basicgraph.py),
[bfs.py](bfs.py), and [queue1210.py](queue1210.py) since
wordLadderStart.py imports them)\
\
Given a \"start\" word and \"end\" word, the Word Ladder game finds a
sequence of intermediate words that transforms the start word to end
word, with the condition that each word in the sequence differs in
exactly one letter (at one position) from the prior and subsequent
words.\
\
Thus, for \"adore\" and \"scorn\" a ladder is: adore adorn acorn scorn\
\
And, for \"white\" to \"black\" a ladder is: white whine shine swine
swing sling cling clink blink blank black\
\
For \"arise\" to \"sleep\" the shortest ladder has 14 intermediate
words! Can you find them?\
\
The wordLadder program takes one optional argument, the name of a text
file containing the word list to be considered. You may assume all words
in the dictionary are five letters long, all lower case. Each word
appears on a separate line in the file. A test file with a few thousand
five-letter words is here: [words5.text](words5.text). NOTE: Test your
code first on a file with just a few words before running your program
on words5.text; debugging will be easier!\
\
Your program should first read the word list and build a corresponding
graph. The graph will have one vertex for each word, and an edge between
nodes whose words differ in exactly letter at one position.\
\
After building the graph, the program should enter a loop that
repeatedly asks the user to provide start and end words, and finds (if
one exists) the shortest word ladder from the start word to the end
word, printing the sequence of words found (or an appropriate message if
no such sequence exists).\
\
\
Note: if you finish this early, here\'s something extra you can do for
fun. Modify your algorithm to try to find *long* word ladders rather
than short ones. E.g. can you find a ladder from black to white that\'s
longer than 100 steps? Longer than 648 steps? (Hint: even just switching
the graph traversal algorithm from bfs to dfs often gives you fairly
long ladders - it\'s super easy to try this \...)\
\
**2.** (4 points) Use randomized simulation to estimate the expected
length of the longest run of consecutive heads in a series of n coin
flips.\
\
For example, in this series of 10 flips:

    T, T, H, T, H, T, H, H, H, T

the length of the longest run of heads is 3.\
\
Start with code in [lec35coins.py](lec35coins.py).\
\
First, modify doNCoinFlips function to return (instead of the numbers of
heads and tails) the length of the longest run of consecutive heads
found in a sequence of n flips.\
\
Next, modify doCoinFlipTrials to collect and process the results of
multiple trials of coin flipping, calculating the average longest run of
heads for the set of trials.\
\
Third, modify doCoinFlipExperiment to calculate and print the expected
longest heads run length for a wide range of numbers of flipped coins.\
\
Finally, in a comment in your .py file, speculate on the mathematical
relationship between the length of the longest heads for for a given
number of coins. I.e. what is the mathematical function relating the
number of coins flipped and the expected/average longest run of heads?
(You might find it easier to guess the function if you modify
plotResults to plot the expected run length versus number of coins
flipped.) Note: you won\'t lose points if you don\'t correctly guess the
function, but give it a try. If you wish, you may search the Internet
for information on this relationship. It\'s fine if you find that
particular answer on the Internet - just be sure to cite your source.

------------------------------------------------------------------------

**Important submission note:** Submit via ICON exactly two files. One
must be a zip file containing four Python files (or a folder containing
the four) for Q1: wordLadder.py (change its name from
wordLadderStart.py!), bfs.py, basicgraph.py (those are the three that
you need to change) and queue1210.py. The other file should be for Q2:
q2.py

------------------------------------------------------------------------

Copyright 2017. James F. Cremer. The University of Iowa
