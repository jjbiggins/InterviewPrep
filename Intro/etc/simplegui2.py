import tkinter

# global variable
counter = 0

# "callback" functions
def increaseBy1():
    global counter
    counter = counter + 1
    updateCountLabel()

def decreaseBy1():
    global counter
    if counter > 0:
        counter = counter - 1
    updateCountLabel()

# "helper" function used by both callbacks
def updateCountLabel():
    countLabel.configure(text="Count: {}".format(counter))


# window, widget and layout specifications
mainWindow = tkinter.Tk()

# frame to hold two side-by-side widgets, the + and - buttons
topFrame = tkinter.Frame(mainWindow)
topFrame.pack()

increaseButton = tkinter.Button(topFrame, text="+", command=increaseBy1)
increaseButton.pack(side=tkinter.LEFT)
decreaseButton = tkinter.Button(topFrame, text="-", command=decreaseBy1)
decreaseButton.pack()

# show the current count in a label below the buttons
countLabel = tkinter.Label(mainWindow, text="Count: 0")
countLabel.pack()

# GO!
#
# mainWindow.mainloop()

# I usually define a separate function that enables additional initialization
# and starts the interaction loop
#
# Call startGUI() after loading this file. Otherwise, depending on your particularl Python IDE,
# the "event loop" might never run and nothing will process any button-pressing that you do.
def startGUI():
    # could do additional initialization here
    # ...
    
    # GO!
    mainWindow.mainloop()
    
