# similar to Exercise 5-5 of textbook

import turtle

def draw(t, angle, length, levelsToDo):
    if levelsToDo == 0:
        return
    t.fd(length)
    t.lt(angle)
    draw(t, angle, int(length*0.8), levelsToDo - 1)
    t.rt(2*angle)
    draw(t, angle, int(length*0.8), levelsToDo - 1)   
    t.lt(angle)
    t.bk(length)

# Try, e.g.,
# runDraw(15, 100, 1)
# runDraw(15, 100, 2)
# runDraw(15, 100, 3)
# runDraw(15, 100, 4)
# runDraw(15, 100, 5)
# runDraw(15, 100, 6)
# Changing the first argument, angle, makes the "tree" branches spread more or less
#
def runDraw(angle, length, levelsToDo):
    turtle1 = turtle.Turtle()
    turtle1.pu()
    turtle1.goto(-2*length, 0)
    turtle1.pd()
    draw(turtle1, angle, length, levelsToDo)

    turtle.mainloop()

