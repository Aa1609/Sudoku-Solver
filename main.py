# importing  libraries
from tkinter import *
import tkinter as tk  
import tkinter.font as font  
from PIL import Image, ImageTk
import os

# making funtion to perform task after user clicks play button

# execution of this function will quiet the current main screen window and will run the game file
# where user can play random sudoku
def play():
    root.destroy()
    os.startfile('gameSudoku.py') # this starts the file passed in method

def userSudoku():
    # place() is used to set location of buttons on the main screen window
    root.destroy()
    os.startfile('userSudoku.py')

def help():
    os.startfile('helpWin.py')

root = tk.Tk()

# set icon of the window
root.wm_iconbitmap('icon.ico')

# title of window
root.title("Sudoku Game & Solver")

# window size
root.geometry("1052x595")
 
# set minimum window size value
root.minsize(1052, 595)
 
# set maximum window size value
root.maxsize(1052, 595)

# calling label funtion
label = tk.Label(root)

# using image as background of window
img = Image.open(r"gameBG.jpeg")
label.img = ImageTk.PhotoImage(img)
label['image'] = label.img
label.pack()

# declaring the font properties 
myFont = font.Font(family='Montserrat', size=15)

# calling Button function
# making 'Play' button
playButton = Button(root, text = 'Play', command = play, bg='#2e2d35', fg='White')
playButton['font'] = myFont
# place() is used to set location of buttons on the main screen window
playButton.place(x=100, y=100, height=100, width=160)

# button to take input of sudoku and solve it 
setButton = Button(root, text = 'Want a solution\nof a Sudoku', command = userSudoku, bg='#2e2d35', fg='White')
setButton['font'] = myFont
# place() is used to set location of buttons on the main screen window
setButton.place(x=265, y=100, height=100, width=160)

# help button to display the rules of the game and solver , also how to use this game and solver
helpButton = Button(root, text = 'Help', command = help, bg='#2e2d35', fg='White')
helpButton['font'] = myFont
# place() is used to set location of buttons on the main screen window
helpButton.place(x=100, y=205, height=100, width=325)

root.mainloop()