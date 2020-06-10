import tkinter

# Set pixel at pos=(column,row) on image, with color=(r,g,b).
def setpixel(image, pos, color):
    r,g,b = color
    column,row = pos
    image.put("#%02x%02x%02x" % (r,g,b), (column, row))
    
# Return tuple (r, g, b) representing color at pixel at pos=(column,row)
def getpixel(image, pos):
    column, row = pos
    stringvalue = image.get(column,row)
    colortuple = tuple(map(int, stringvalue.split()))
    return(colortuple)

# Change image to grayscale
def makeGrayscale(image):
    height = image.height()
    width = image.width()
    for row in range(height):
        for col in range(width):
            orig = getpixel(image, (col,row))
            avg = (orig[0] + orig[1] + orig[2])//3
            new = (avg, avg, avg)
            setpixel(image, (col,row), new)
            

# Change image to negative of original
def makeNegative(image):
    height = image.height()
    width = image.width()
    for row in range(height):
        for col in range(width):
            orig = getpixel(image, (col,row))
            new = (255-orig[0], 255-orig[1], 255-orig[2])
            setpixel(image, (col,row), new)

def flipLeftRight(image):
    height = image.height()
    width = image.width()
    
    for row in range(height):
        x = width-1
        for col in range(width//2):
            origRight = getpixel(image,(x,row))
            origLeft = getpixel(image, (col,row))
            setpixel(image,(x, row),origLeft)
            setpixel(image,(col, row),origRight)
            x = x-1
    
    return                             

def flipUpDown(image):
    height = image.height()
    width = image.width()
    for col in range(width):
        y = height-1
        for row in range(height//2):
            origLower = getpixel(image, (col,y))
            origUpper = getpixel(image, (col, row))
            setpixel(image,(col,y),origUpper)
            setpixel(image, (col, row), origLower)
            y = y-1
    return

# make image "redder"           
def customChange(image):
    height = image.height()
    width = image.width()
    for row in range(height):
        for col in range(width):
            orig = getpixel(image, (col,row))
            newRed = min(255, int(1.2*orig[0]))
            new = (newRed, orig[1], orig[2])
            setpixel(image, (col,row), new)
    return

def click(operation):
    global label2
    global photo2
  
    if operation == "grayscale":
        makeGrayscale(photo2);
    elif operation == "negative":
        makeNegative(photo2)
    elif operation == "horiz":
        flipLeftRight(photo2)
    elif operation == "vertical":
        flipUpDown(photo2)
    elif operation == "custom":
        customChange(photo2)
    elif operation == "orig":
        photo2 = tkinter.PhotoImage(file = imagefilename)
    else:
        print("Oops, this should never occur (in click function)")
        return
    label2.image = photo2
    label2.configure(image=photo2)

# Code presumes giffilename is the name of a gif image file
# of dimensions 400x300
#
def editImage(giffilename):
 
    global imagefilename
    global photo2
    global label  
    global label2
    
    imagefilename = giffilename
    
    rootWindow = tkinter.Tk()
    mainframe = tkinter.Frame(rootWindow, height=360)
    mainframe.pack()
    imageframe = tkinter.Frame(mainframe, width=830, bd=2, relief=tkinter.GROOVE)
    imageframe.pack()
  
    photo = tkinter.PhotoImage(file = imagefilename)
    photo2 = tkinter.PhotoImage(file = imagefilename)


    label= tkinter.Label(imageframe, image=photo)
    label2 = tkinter.Label(imageframe, image=photo2)
    
    label.grid(row=0, column=0)
    label2.grid(row=0, column=1)
    
    nbutton = tkinter.Button(mainframe, text="grayscale", command=lambda : click("grayscale"))
    nbutton.pack()
    nbutton2 = tkinter.Button(mainframe, text="negative", command=lambda : click("negative"))
    nbutton2.pack()
    nbutton3 = tkinter.Button(mainframe, text="flip horizontally", command=lambda : click("horiz"))
    nbutton3.pack()
    nbutton4 = tkinter.Button(mainframe, text="flip vertically", command=lambda : click("vertical"))
    nbutton4.pack()
    nbutton5 = tkinter.Button(mainframe, text="custom change", command=lambda : click("custom"))
    nbutton5.pack()
    nbutton5 = tkinter.Button(mainframe, text="restore original", command=lambda : click("orig"))
    nbutton5.pack()
    
    rootWindow.mainloop()
    
