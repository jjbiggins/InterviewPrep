**Homework 4**\
CS1210 Computer Science 1\
Due Wednesday, February 22, by 9:00am\
10 points\
\

**1.** Download and follow the instructions in
[hw4q1start.py](hw4q1start.py) to complete an interactive program that
prints information about \"neighbor\" words in a file of words.\
\
*Do not* add any additional functions to the file. *Do not* change the
names of any functions in the file.\
\
*Do* \"clean up\" the file as you complete the work, eliminating the
instruction comments. In the end the file should have only comments that
make sense for a finished program.\
\
Sample word files:

-   [wordsTest.txt](wordsTest.txt) (contains only 7 words. Test with
    this first!)
-   [words5000.txt](words5000.txt) (contains the 5000 most commonly used
    English words according to <http://www.wordfrequency.info/>
-   [words5.txt](words5.txt) (contains 2415 five-letter words)

\
**2**. Write a recursive function makeChange(amount, coinVal1, coinVal2,
coinVal3) that determines whether or not change for amount (where amount
is an integer), can be made using coins (any number of them) of the
three given integer values. If the answer is yes, the function should
return a list of a coin values totalling amount. Otherwise, return
False.\
\
For example:

    >>> makeChange(64, 5, 11, 13)
    [13, 11, 5, 5, 5, 5, 5, 5, 5, 5]
    >>> makeChange(7, 3, 5, 12)
    False

No loops are needed nor allowed. Use only if statements, recursion, and
simple math operations.\
\
**3.** Write a recursive function areSimilar(item1, item2) that returns
True or False depending on whether or not the two given input items are
similar according to the following definition.\
\
Two items are similar if:

1.  they are the same type, and
2.  *if* they are lists, they are of the same length and each pair of
    corresponding list items (i.e. items with the same index) is
    similar.

For example,

    >>> print(areSimilar(True, False))                   items are same type and are not lists
    True
    >>> print(areSimilar(1, 'a'))                        items are different types
    False
    >>> print(areSimilar([],[]))                      
    True                        
    >>> print(areSimilar([],[3]))                        list lengths differ
    False
    >>> print(areSimilar([3.0],[3]))                     lists of same length but index 0 items are not similar
    False
    >>> print(areSimilar([5],[3]))                       lists of same length and corresponding lists items are similar
    True
    >>> print(areSimilar([1,2,['a','b']],[3,4, [1,2,3]]))      items at index 2 are not similar
    False
    >>> print(areSimilar([1,2,[False, 'b']],[3, 4, [True, 'hello']]))
    True
    >>> print(areSimilar([[[[],[2],[],['hi', [0]]]]], [[[[],[-2],[],['bye', [1]]]]]))
    True
    >>> print(areSimilar([[[[],[2],[],['hi', [0]]]]], [[[[],[-2],[],['bye', 0]]]]))
    False

**4.** Write functions testQ2() and testQ3() that test your Q2 and Q3
functions on a variety of input values.\
\

------------------------------------------------------------------------

Submit to ICON exactly two Python files, one for Q1, and one containing
the answers for the Q2, Q3, and Q4. The files must not contain any code
that is not part of a function definition.
