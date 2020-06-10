import tkinter

# callback functions

def buttonPushed():
    textInEntry = textEntry.get()
    textEntry.delete(0, tkinter.END)
    print(textInEntry)



# Create main window
mainWindow = tkinter.Tk()

# Create a Frame (called 'container') to hold two side-by-side widgets, the label and the entry
container = tkinter.Frame(mainWindow)
container.pack()
                  
label = tkinter.Label(container, text="Enter some text:")
label.pack(side=tkinter.LEFT)
textEntry = tkinter.Entry(container)
textEntry.pack()

# Create a button and put it beneath the container.
# Specify buttonPushed as "callback" function that gets called when the button is pressed.
button = tkinter.Button(mainWindow, text="Print entry text in shell", command=buttonPushed)
button.pack()

# GO!
mainWindow.mainloop()
