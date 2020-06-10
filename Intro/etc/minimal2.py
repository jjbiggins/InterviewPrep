import tkinter

# define "callback" functions - programmed responses to events in GUI

def button1pushed():
    print("You pushed button1!")

def button2pushed():
    print("You pushed button2!")

def button3pushed():
    print("You pushed button3!")
    
# create widgets and speicify GUI layout 

window = tkinter.Tk()
window.title("Simple tkinter window")

# the main window, window, will contain two Frames, window subregions that will
# each contain a few widgets. Using Frames helps with customizing overall layout.
# You can treat a Frame like any other widget and control where it goes within its
# parent container (here, the main window).  And within a frame you can control
# how its own widgets lay out.
# topFrame will contain three Labels, arranged horizontally (within the frame)
# bottomFrame will contain three Buttons, arranged vertically (within the frame).
# The two frames will be arranged vertically, topFrame above bottomFrame.

# First create the top frame
topFrame = tkinter.Frame(window)
topFrame.pack()

# Create labels 1, 2 ,and 3 with topFrame as their container.
label1 = tkinter.Label(topFrame, text = "This is a label.")
label1.pack(side=tkinter.LEFT)

label2 =  tkinter.Label(topFrame, text = "This is a another label.", relief = tkinter.GROOVE, fg = "red")
label2.pack(side = tkinter.LEFT)

label3 =  tkinter.Label(topFrame, text = "This is a third label.")
label3.pack()

# Now create the second frame, bottomFrame
bottomFrame = tkinter.Frame(window)
bottomFrame.pack()

# Add three buttons to bottom frame
button1 = tkinter.Button(bottomFrame, text = "Push me", command = button1pushed)
button1.pack()

button2 = tkinter.Button(bottomFrame, text = "Push me!", command = button2pushed)
button2.pack()

button3 = tkinter.Button(bottomFrame, text = "No, push me!!", command = button3pushed)
button3.pack()
    
# GO! i.e. start the GUI loop that will respond to events like button presses.

window.mainloop()

