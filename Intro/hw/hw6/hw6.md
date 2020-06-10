CS1210 Homework 6

**Homework 6**\
CS1210 Computer Science 1\
Due Wednesday, March 29, by 11:59pm\
10 points\
\

**1.** Create a Box class, representing rectangular 3D boxes. The boxes
can be any size and can be located anywhere in 3D space, but in this
simple version their orientations are fixed so that their edges are
always aligned with/parallel to coordinate system axes. You class must
implement all the methods below:

-   \_\_init\_\_(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0,
    width = 1.0, height = 1.0, depth = 1.0)
-   setCenter(self, x, y, z)
-   setWidth(self, width)
-   setHeight(self, height)
-   setDepth(self, depth)
-   volume(self)
-   surfaceArea(self)
-   overlaps(self, otherBox)
-   contains(self, otherBox)
-   \_\_repr\_\_(self)

Note that \"width\" is a box\'s extent along the x dimension, while
\"height\" and \"depth\" are the y and z extents, respectively.\
box1.overlaps(box2) should return True if the two 3D boxes
touch/intersect at all (even they just touch exactly at their edges or
corners).\
box1.contains(box2) should return True if no point of box2 is outside of
box1\
*Note: think carefully about the overlaps and contains test. It is easy
to get these wrong. I recommend (before you start coding) sketching some
pictures to help you analyze the possibilities.*\
\
Use of the class in a Python shell might look like this:

       >>> box1 = Box(10.0, 5.0, 0.0, 2.0, 1.0, 1.0)
       >>> box1
       < 2-by-1-by-1 3D box with center at (10.0, 5.0, 0.0) >
       >>> box2 = Box(0, 0, 0, 3.5, 2.5, 1.0)
       >>> box1.volume()
       2.0
       >>> box2.surfaceArea()
       29.5
       >>> box1.overlaps(box2)
       False
       >>> box1.setCenter(2.75, 0.0, 0.0)
       >>> box1.overlaps(box2)
       True
       >>> box1.setCenter(2.76, 0.0, 0.0)
       >>> box1.overlaps(box2)
       False
       >>> box1.setCenter(2.75, 1.75, 1.0)
       >>> box1.overlaps(box2)
       True
       >>> box1.setCenter(0.0, 0.0, 0.0)
       >>> box1.overlaps(box2)
       True
       >>> box1.setWidth(50.0)
       >>> box1.overlaps(box2)
       True
       >>> box1.setDepth(50.0)
       >>> box2.overlaps(box1)
       True
       >>> box3 = Box(0, 0, 0)
       >>> box2.contains(box3)
       True
       >>> box4 = Box(10.0, 5.0, 0.0, 2.0, 1.0, 1.0)
       >>> box4.contains(box3)
       False 

As part of your .py file for this problem, include a testBox function
that demonstrates use of the Box class, printing helpful output.\
\
**2.** Create a NimGame class that implements the simplest form of
two-player Nim-style games (<http://en.wikipedia.org/wiki/Nim>),
sometimes called the \"subtraction game.\" The game starts with some
specific number of items - pebbles, coins, matchsticks, balls. Players
take turns removing between 1 and 3 items. The player who removes the
last item wins. You can play an interactive on-line version of the game
here:
<http://upload.wikimedia.org/wikipedia/commons/4/4d/Subtraction_game_SMIL.svg>\
\
For this assignment, we\'ll keep things very simple. Assume there\'s one
human player playing against the computer and that the human always goes
first.\
To create the NimGame class, you only need to implement two methods:

1.  an \_\_init\_\_ method, with an argument specifying how many items
    (call them \"balls\") the game should start with
2.  a remove method, with an argument specifying how many balls the
    human player wishes to remove. This method should check that the
    specified number of balls is valid and, if so, remove that many
    balls, and check whether or not the player has lost. Next, it should
    automatically select a (legal) number of balls for the computer to
    remove (either randomly or through a \"smart\" strategy), and it
    should update the game state accordingly (and check whether the
    computer has lost).

A sample use of the class might produce these results:

       >>> game = NimGame(12)
       Nim game initialized with 12 balls.
       >>> game.remove(2)
       You took 2 balls. 10 remain.
       Computer took 3 balls. 7 remain.
       >>> game.remove(1)
       You took 1 ball. 6 remain.
       Computer took 2 balls. 4 remain.
       >>> game.remove(1)
       You took 1 ball. 3 remain.
       Computer took 3 balls. 0 remain.
       Computer wins!

\
\
**3.** Add one additional subclass of Animal, including at least one new
method, to the code in [animals.py](animals.py). As part of your new .py
file (which will contain the original code from animals.py plus your new
class), include a testAnimals() function that demonstrates use of your
new class.\
\

------------------------------------------------------------------------

Submit via ICON exactly three Python files (or one .zip file containing
three .py files), one for each question. The files must not contain any
top-level code that is not an import statement or part of a function or
class definition.

------------------------------------------------------------------------

Copyright 2017. James F. Cremer. The University of Iowa
