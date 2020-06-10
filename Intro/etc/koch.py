"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

''' modified by Jim Cremer 2/22/16'''

import turtle

def koch(t, length, levelsToDo):
    """Draws a koch curve with length n."""
    if levelsToDo == 0:
        t.fd(length)
        return
    newLength = length // 3
    koch(t, newLength, levelsToDo-1)
    t.lt(60)
    koch(t, newLength, levelsToDo-1)
    t.rt(120)
    koch(t, newLength, levelsToDo-1)
    t.lt(60)
    koch(t, newLength, levelsToDo-1)


def snowflake(t, length, levelsToDo):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, length, levelsToDo)
        t.rt(120)

# Try
# runKoch(300, 0)
# runKoch(300, 1)
# runKoch(300, 2)
# runKoch(300, 4) - will probably take several minutes
#
def runKoch(length, levelsToDo):
    turtle1 = turtle.Turtle()

    turtle1.pu()
    turtle1.goto(-length//2, length//2 )
    turtle1.pd()
    snowflake(turtle1, length, levelsToDo)

    turtle.mainloop()

