CS1210 Homework 3

**Homework 3**\
CS1210 Computer Science 1\
Due Monday, February 13, by 9:00am\
10 points\
\
NOTE: You may not use any functions from external modules loaded by
\'import.\' In addition, you may not use dictionaries, list
comprehensions, or other Python language features not yet taught in this
class. The point of these exercises is to practice very basic components
of programming.\
\

**1.** Write a function, printStringStats(inputString), that takes as
input a string of lowercase letters and prints three things: the
lexicographically largest letter (z \> y \> \... \> a), the third
largest letter, and the most common letter along with how many times it
occurs.\
\
You may assume the string is at least one character long. But you may
not assume that it contains at least three different characters. If
fewer than three different letters appear in the string, print something
appropriate for the third largest (e.g. \"There is no third largest
letter.\")\
\
If two or more letters tie for most common, you may choose any one of
them.\
\
For example:

    >>> printStringStats('aaczzcqzqqqzqc')
    In 'aaczzcqzqqqzqc', the largest letter is 'z', the third largest letter is 'c',
     and the most common letter is 'q', occurring 5 times

    >>> printStringStats("aaaaba")
    In 'aaaaba', the largest letter is 'b', there is no third largest letter,
     and the most common letter is 'a', occurring 5 times
       

NOTE: you may *not* use built-in min, max, sort, or sorted functions.
You may not use any built-in string methods. Use one or more simple
loops, and simple comparison (\<,\>, ==, !=) operators only.\
\
**2.** Write a function primeDivisorsOf(num) that takes a positive
integer as input and returns a list of that number\'s prime divisors.
You may copy and use the numIsPrime function developed in class if you
wish.\
\
For example:

    >>> primeDivisorsOf(36)
    [2,3]
    >>> primeDivisors(23)
    [23]
    >>> 
    >>> primeDivisorsOf(5003*5003+1)
    [2, 5, 2503001]
    >>> primeDivisorsOf(4)
    [2]
    >>> primeDivisorsOf(1)
    []

**3.** Write function, innerMin(listOfLists), that takes as input a list
of zero or more sublists each containing zero or more numbers, and
determines and prints 1) minimum number among all of the sublists and 2)
the sublist containing that minimum.\
\
You may assume there is no tie for the minimum. I.e, *if* there is a
minimum, it is unique. If, however, there is no minimum, innerMin should
print an appropriate message.\
\
For example:

    >>>innerMin([[6, 7], [9, 4, 6]])
    In [[6, 7], [9, 4, 6]] the min item is 4 and is found in sublist [9, 4, 6]

You should use nested loops for this problem, an outer loop iterating
over items (sublists) of the main list, and an inner loop stepping over
items (numbers) in the sublists. In the inner loop, only simple
comparisons should be used. Once again, you may not use built-in
functions min, max, sort or sorted for this problem.\
\
**4.** Write functions testQ1(), testQ2(), and testQ3() that test your
Q1, Q2, and Q3 functions on a variety of input values. For example, for
some imagined function foo(n1, n2), a test function and its output might
be:

    def testFoo():
        print("foo(2,3) returns {}".format(foo(2,3)))
        print("foo(5, -1) returns {}".format(foo(5, -1)))
        print("foo(100, -23) returns {}".format(foo(100, -23)))

    >>> testFoo()
    foo(2,3) returns 2
    foo(5, -1) returns 6
    foo(100, -23) returns -24

Note: most good test functions should contain more than three tests!\
\

------------------------------------------------------------------------

Submit to ICON one python file containing all the required functions.
The file must not contain any code that is not part of a function
definition.
