from tkinter import Tk, Canvas, Frame, Button, LEFT, RIGHT, SUNKEN
from time import sleep

# global variables used for placement of towers and disks
canvassHeight = 250
canvassWidth = 650

halfTowerWidth = 100
towerHeight = 120
towerBaseThickness = 5
towerSpindleHalfWidth = 2

diskHeight = 20
tower1x = 15 + halfTowerWidth
tower2x = tower1x + 10 + 2*halfTowerWidth
tower3x = tower2x + 10 + 2*halfTowerWidth
towersBottom = canvassHeight - 50

# a Stack-like class that maintains information about one tower and its disks
#
class Tower():
    def __init__(self, xposition, initialItems = []):
        self.items = initialItems
        self.xposition = xposition
    def isEmpty(self):
        return(len(self.items) == 0)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return(self.items.pop())
    def top(self):
        return(self.items[-1])
    def numItems(self):
        return(len(self.items))

# Movie the top disk on fromTower to the top of ToTower.
#   - fromTower and toTower must both be Tower objects.
#   - This function will:
#     1) update both Tower objects, and also
#     2) display the result on the canvas.
#
def move(fromTower, toTower):
    global canvas
    if (fromTower.isEmpty()):
        return
    id1 = fromTower.pop()
    currCoords = canvas.coords(id1)
    xchange = toTower.xposition - fromTower.xposition
    ychange = - (toTower.numItems() - fromTower.numItems()) * diskHeight 
    canvas.coords(id1,
                  currCoords[0] + xchange,
                  currCoords[1] + ychange,
                  currCoords[2] + xchange,
                  currCoords[3] + ychange)
    # Normally, it wouldn't make sense to put this delay in here.
    # However, putting it here allows the Towers of Hanoi
    # solver be  independent of graphics and waiting.
    # Without the wait, the graphics updates might be too fast to see
    # when the automatic solve is used.
    # You can make the argument to "sleep" smaller or larger (the
    # unit is seconds).  
    sleep(1.0)
    # The 'update_idletasks()" is used to "flush" graphics updates - that
    # is, it makes them appears immediately after execution.  Without this
    # line, the GUI system will often wait until a bunch of updates have been
    # specified and show them all at once. But in this case, we want to see
    # every update during, for instance, the automatic solution.
    canvas.update_idletasks()
    toTower.push(id1)

def solveToH(n, fromTower, toTower, tempTower):
    if n == 0:
        return
    else:
        solveToH(n-1, fromTower, tempTower, toTower)
        move(fromTower, toTower)
        solveToH(n-1, tempTower, toTower ,fromTower)
        
def initializeAndSolve():
    initializeToH()
    solveToH(numDisks, tower1, tower2, tower3)

# Draws the base and "pole"/spindle that the disks are placed upon to create
# the tower.
#
# You should not need to change this function.
#
def drawSpindle(tower):
    canvas.create_rectangle(tower.xposition - halfTowerWidth,
                            towersBottom,
                            tower.xposition + halfTowerWidth,
                            towersBottom + towerBaseThickness,
                            fill = "black")
    
    canvas.create_rectangle(tower.xposition - towerSpindleHalfWidth,
                            towersBottom - towerHeight,
                            tower.xposition + towerSpindleHalfWidth,
                            towersBottom,
                            fill = "black")

# Create the three Tower objects, initialize tower1 with the desired
# number of disks, and draw the initial setup.
#
# You should not need to change this function.
#
def initializeToH():
    global tower1, tower2, tower3
    global canvas
    canvas.delete("all")
    
    tower1 = Tower(tower1x, [])
    tower2 = Tower(tower2x, [])
    tower3 = Tower(tower3x, [])
    drawSpindle(tower1)
    drawSpindle(tower2)
    drawSpindle(tower3)
    for i in range(numDisks):
        disk = canvas.create_rectangle(tower1.xposition - (numDisks-i)*diskHeight,
                                       towersBottom-(diskHeight*(i+1)),
                                       tower1.xposition + (numDisks-i)*diskHeight,
                                       towersBottom-(diskHeight*i),
                                       fill="#9999ff")
        tower1.push(disk)

 
# widgets and layout for Towers of Hanoi application
def initializeGUI():
    global root
    global canvas
    root = Tk()
    canvas = Canvas(root, height=canvassHeight, width=canvassWidth, relief=SUNKEN, borderwidth=2)
    canvas.pack(side=LEFT)

    buttonframe = Frame(root)
    button1 = Button(buttonframe, text='1->2', command=lambda: move(tower1,tower2))
    button2 = Button(buttonframe, text='1->3', command=lambda: move(tower1,tower3))
    button3 = Button(buttonframe, text='2->1', command=lambda: move(tower2,tower1))
    button4 = Button(buttonframe, text='2->3', command=lambda: move(tower2,tower3))
    button5 = Button(buttonframe, text='3->1', command=lambda: move(tower3,tower1))
    button6 = Button(buttonframe, text='3->2', command=lambda: move(tower3,tower2))
    button7 = Button(buttonframe, text='Initialize', command=initializeToH)
    button8 = Button(buttonframe, text='Solve', command=initializeAndSolve)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
    buttonframe.pack(side=RIGHT)


# Call 'runToH' with the number of desired disks as argument
#
def runToH(numberOfDisks):
    global numDisks
    global root
    
    if ((numberOfDisks < 1) or (numberOfDisks > 10)):
        print("Error: runToH can only handle 1 to 10 disks")
        return
    numDisks = numberOfDisks
    initializeGUI()
    initializeToH()
    root.mainloop()



