**Homework 9**
CS1210 Computer Science 1
Due Sunday, April 30, by 5:00pm
10 points

**1.** (5 points) Modify nimGameWithGUI.py so that a user can interactively play Nim (the game from HW 6, Q2). The provided file already works. Load it
into Python and execute runNim(6) to see what it does. Your assignment is to improve it.

Minimum requirements (worth 4 out of 5 points):
- replace the Label widget that displays as "!replace!" in the GUI (and is named placeHolder in the code) with an Entry widget. When the "New - ---- Game" button is pressed, the initial number of balls in the new game should be the number in the Entry widget.
whenever fewer than three balls remain, inactivate the buttons that would result in illegal moves.
- use the status Label (statusLabel in the code) to provide more feedback to the player. Remove the code that prints information to the Python shell, and instead use the status label to display information such as how many balls the computer took, win/lose status ("You win!" or "Computer wins!"), etc.

- replace the Label widget that displays as "!replace!" in the GUI (and is named placeHolder in the code) with an Entry widget. When the "New
- Game" button is pressed, the initial number of balls in the new game should be the number in the Entry widget.
whenever fewer than three balls remain, inactivate the buttons that would result in illegal moves.
- use the status Label (statusLabel in the code) to provide more feedback to the player. Remove the code that prints information to the Python shell,
and instead use the status label to display information such as how many balls the computer took, win/lose status ("You win!" or "Computer
wins!"), etc.

Make one or more additional changes of your own choice to improve the game (worth 1 out of 5 points). Possibilities include:


- Maintain and display a count of how many games have been won/lost by the player and the computer.
- Modify GUI layout, change colors, etc.
- improve the graphics via one or more of:
-- put numbers in the centers of (or underneath) the balls so it's easier for the player to quickly see how many are left,
change the drawing code so that the balls appear on the screen in a more pleasing way (perhaps all at once rather than the current one-at-a-
time refresh)
-- the 1-second delay between balls removed by player and computer seems clunky. Think of a way to make that nicer.
-- provide "fancier" win/lose status information using the canvas/graphics area rather than the status label.
- change ball graphics. E.g. make balls look more nicer, or lay them out differently on canvas (perhaps several rows of balls if there are a lot of
them)

**2.** Modify hw10start.py in five ways:

- add a Tkinter Entry widget to the GUI so that you can enter an address string (e.g. "Iowa City, IA" or "Beijing, China"). You probably should also
 add a Label widget near the Entry widget saying something like "Enter the location: ".
- modify the readEntryAndShowMap function so that it creates and displays a new map based on the address given in the Entry widget
- add buttons or a slider or other widget(s) to enable changing the map zoom level, redisplaying the map each time the zoom level is changed. You
may choose your own way to do this. One way would be to use two buttons (e.g. one labeled '+' and one labeled '-', like in the simplegui2.py code in
the April 17 lecture notes). Clicking on either of them would change the current zoom level by 1 and recompute and redisplay the map.
- provide a way to change between standard (road) map view and satellite, terrain, and hybrid map views
- display a map pin in the center of the map. Note: for this and the previous item, in addition to adding GUI elements, you will need to modify
getMapURL to add more parts to the string sent to Google.

Submit to ICON exactly two files, nimGameWithGUI.py and one for Q2 (or one zip file containing those two .py files)

Copyright. 2017. James F. Cremer. The University of Iowa


