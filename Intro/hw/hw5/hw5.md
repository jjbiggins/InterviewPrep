CS1210 Homework 5

**Homework 5**\
CS1210 Computer Science 1\
Due Friday, March 10, by 5:00pm\
10 points\
\

------------------------------------------------------------------------

**1. (6 points)**\
**a.** Write a program, hamAndSpam(smsFilename), that analyzes word
frequencies in real-world text messages.\
\
Text file [SMSSpamCollection.txt](SMSSpamCollection.txt) contains 5574
SMS messages. There is additional information about the contents of the
file in the associated \"readme\" file
[readmeSMSSpamCollection.txt](readmeSMSSpamCollection.txt), written by
the creators of the dataset. The data was originally from this
no-longer-working link:
http://www.dt.fee.unicamp.br/\~tiago/smsspamcollection/. Some
information about the data set and its initial investigators is now
[here](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection).\
\
Each line of the file is represents one SMS/text message. The first item
on every line is a label - \'ham\' or \'spam\' - indicating whether that
line\'s SMS is considered spam or not. The rest of the line contains the
text of the SMS/message. For example:

    spam  Congrats! 1 year special cinema pass for 2 is yours. call 09061209465 now! Call ...
    ham Sorry, I'll call later in meeting.

At the end, your program must print summary information and information
about the most frequent words in spam messages and the most frequent
words in non-spam (ham) messages. It should also compute and compare the
average lengths of spam and ham messages. I will not specify exactly
what your output should be (but I will demonstrate sample output during
the next lecture or two. I will also provide organizational hints and
help for each of the parts).\
\
To accomplish this, your hamAndSpam function should:

-   read all of the data from the input file
-   extract individual words from the messages. This should include an
    effort to get ride of \"extras\" such as periods, commas, question
    and exclamation marks, and other characters that aren\'t part of a
    word. You should probably also ignore capitalization. Thus in the
    sample spam message above, you probably want to treat \"Congrats!\"
    as \"congrats\" in your frequency analysis.
-   build two dictionaries (required for full credit on this
    assignment), one for frequencies of words appearing in spam
    messages, one for frequencies of words from ham messages.
-   print summary information and some word frequency information about
    the data.

Again, it is up to you to decide exactly what to print, though it must
include some word frequency and message length information as mentioned
above. Summary information might include the number of spam/non-spam
messages, the total number of different words in spam and non-spam
messages, the total number of words in each, and anything else that
might be interesting (does spam or non-spam have longer average word
length?? longer message length??). Frequency information might be in the
form of the top ten most used words in spam and in non-spam, along with
a measure of their frequency (is a absolute number of occurrences a good
measure? Or might it be better to use a fraction/percentage of all
occurrences in that type of message). Possibly also consider printing
information about most frequent words with more than, say, one or two or
three letters - the results might be more enlightening. (You could also,
but it is not required, compare the results with the list of 5000 most
common English words of the file words5000.txt - most common word first
- from HW4.)\
\
**b.** Write a couple of sentences/short paragraph saying something
about the results. Can you conclude something about spam vs. non-spam?
Did you learn something?\
*Put this answer as a comment at the top of your .py file.*\
Thus, your file should look like:

    # 1b. ... your answer here ...
    #    ....
    #

    #
    def hamAndSpam(smsFilename):
     ...

\
**2.** (2 points) Consider the following function

    import random
    # Assumption: listOfList is a list of 0 or more non-empty lists
    #
    def randChoices(listOfLists):
        result = []
        for sublist in listOfLists:
            chosenItem = random.choice(sublist)
            result.append(chosenItem)
        return result

First, study (and test) randChoices to determine what it does (as part
of this, look up what the random module\'s choice function does). Then
re-write randChoices so that it accomplishes the same task with a
one-line list comprehension. Thus, the new function will have exactly
two lines, the def line and a return line containing a list
comprehension expression.\
\
**3.** (2 points) A common kind of puzzle question is \"how many numbers
between 1 and 10000 contain the digit 9?\". Write a function
howManyNumsWithDigit(maxNumber, digit) that returns the number of
numbers from 1 through maxNumber that contain the given digit.\
\
For example howManyNumsWithDigit(10, 5) should return 1,
howManyNumsWithDigit(10,1) should return 2, and howManyNumsWithDigit(40,
2) should return 13.\
Your function must use a list comprehension (but remember, it returns a
number not a list!) and have only one line of code (in addition to the
def line).\
\
Note: of course, there are ways to solve this problem that don\'t use
list comprehensions. But, for this assignment, you must use a list
comprehension. Use a list comprehension to create a list of all the
numbers that contain the digit, and then simply return the length of
that list.\
\

------------------------------------------------------------------------

Submit to ICON exactly two Python files, one for question 1, and one
containing the answers for both questions 2 and 3. The files must not
contain any code that is not part of a function definition.

------------------------------------------------------------------------

Copyright. 2017. James F. Cremer. The University of Iowa
