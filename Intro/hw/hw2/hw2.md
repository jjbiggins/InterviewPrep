CS1210 Homework 2

**Homework 2**\
 CS1210 Computer Science 1\
 Due Monday, February 6, by 9:00am\
 10 points \

**1.** Function printRanges(7, 3) produces the following output:

    7
    0 1 2 3 4 5 6  
    6
    0 1 2 3 4 5
    5
    0 1 2 3 4 
    4
    0 1 2 3 
    3
    0 1 2

Write function printRanges(high, low) that produces output according to
the rule implied by the example output. You may assume high and low are
positive integers with high \>= low. You function \*must\* contain two
loops, one nested within the other. Your function may not use any
comprehensions, string operations, range, or list functions; the goal is
to practice loops and incrementing. \
\
 **2.** Write a function printVowelStats(inputString) that calculates
and prints the number of occurrences of each vowel (consider the vowels
to be only: a/A, e/E, i/I, o/O, and u/U) in the string and also the
total number of non-vowels. NOTE: You must use a loop to count the vowel
occurrences. You many *not* use the Python's built-in count function. \
\

    >>> printVowelStats("Octopus")

should print:

    'Octopus' has 0 'a's, 0 'e's, 0 'i's, 2 'o's', 1 'u's, and 4 non-vowels.

\
 **3.** Write function, leastChar(inputString) that takes as input a
string of one or more letters (and no other characters) and prints 1)
the "least" character in the string, where one character is less than
another if it occurs earlier in the alphabet (thus 'a' is less than 'C'
and both are less than 'y') and 2) the index of the first occurrence of
that character. When comparing letters in this problem, *ignore* case -
i.e. 'e' and 'E' should be treated as equal. However, your output should
use the case of the least letter as it appears in the input. Thus, in
the example below "The least char is 'b' ..." would be incorrect.\
\
 Important: your function must contain exactly one loop and you must
determine the index of the character within the loop (i.e. you may not
use Python's min, index, or find, and you may not use any lists). You
may, however, use Python's lower() function to help with string case.

    For example,

    >>> leastChar("yRrcDefxBqubSlyjYelskd")

should yield:

    The least char is 'B' and occurs at position 8.

**4.** Implement function generateSequence(startNumber, factor, offset,
stopNumber) that generates a sequence of numbers as follows. The
sequence starts with startNumber. Let currNumber represent the current
number in the sequence. Then, until the currNumber is equal to
stopNumber, the following rule is used to update currNumber:

-   if currNumber is even, the next number is currNumber / 2.
-   if currNumber is odd, then next number is ((currNumber \* factor) +
    offset)

Assume all inputs are positive integers and that startNumber is greater
than or equal to stopNumber. generateSequence should 1) print each
number of the sequence on a separate line, and 2) print information
about the length of the sequence (i.e. the number of numbers generated
in the sequence). Your function should use a single while loop. For
example:

    >>> generateSequence(5, 3, 3, 3)
    5
    18
    9
    30
    15
    48
    24
    12
    6
    3
    Length of sequence:  10

    >>> generateSequence(5, 3, 1, 1)
    5
    16
    8
    4
    2
    1
    Length of sequence:  6

Note: for some input values, the sequence will not terminate! That's
okay! Play with various small values of factor, offset, and stopNumber.
For example, try various combinations of 1, 2, and 3 for factor, offset,
and stopNumber. \
\

* * * * *

Submit to ICON one python file containing the four required functions.
The file must not contain any code that is not part of a function
definition. \
\
 You may (but are not required to) add additional functions that you use
for testing the required. In general, it is excellent practice to
include a function that tests your other code. For example, you might
write a function, "def testMyHWFunctions(): ..." that makes several
calls to each of your homework functions using a variety of input
values.
