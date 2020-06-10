import tkinter

window = tkinter.Tk()

def radioButtonChosen():
    global selectedButton
    if choiceVar.get() == 1:
        selectedButton = "one"
    else:
        selectedButton = "two"
    label.configure(text= "radio button choice is: {}".format(selectedButton))

selectedButton = "one"   
choiceVar = tkinter.IntVar()
choiceVar.set(1)

choice1 = tkinter.Radiobutton(window, text="one", variable=choiceVar, value=1,
                  command=radioButtonChosen)
choice1.pack()

choice2 = tkinter.Radiobutton(window, text="two", variable=choiceVar, value=2,
                  command=radioButtonChosen)
choice2.pack()

label = tkinter.Label(window, text = "radio button choice is: {}".format(selectedButton))
label.pack()

def startGUI():
    global selectedButton
    window.mainloop()
