# impoting libraries
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from dokusan import generators
import numpy as np
import os

# variable to store the number of rows or column in sudoku
M = 9

def solve(sudoku, row, col, num):
    # this code is checking it the number filled in a cell is unique in both respective row and column
    
    for x in range(9):
        # if same number is found in row function will return false to solver
        if sudoku[row][x] == num:
            return False
             
    for x in range(9):
        # if same number is found in column function will return false to solver
        if sudoku[x][col] == num:
            return False
 
    # making start counter for 3x3 grid as they also conation unique number
    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            # if same number is found in 3x3 grid function will return false to solver
            if sudoku[i + startRow][j + startCol] == num:
                return False

    # if all the test passes, means sudoku is found correct then the funtion will return true to the solver 
    return True


# this is where all the number from 0 to 9 gets checked using for loop and calling the above solve function passing the iteration variable as the parameter which is here number to be flled
def Suduko(sudoku, row, col):
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0

    # checking if the cell is filled with non-zero number
    if sudoku[row][col] > 0:
        # starting the sudoku solver again, recursion call is done to move to the next column
        return Suduko(sudoku, row, col + 1)

    for num in range(1, M + 1, 1): 
     
        if solve(sudoku, row, col, num):
            # chaning the sudoku list number to check sudoku
            sudoku[row][col] = num

            #  if the number replaced is correct then the funtion will return true
            if Suduko(sudoku, row, col + 1):
                return True
        
        # setting again to zero if the number replaced was not correct
        sudoku[row][col] = 0
    return False


# this funtion is bind to solve button and it changes the whole game window
def SolvedUI(sudoku):
    for i in range(9):
        for j in range(9):
            # below two lines of code is to delete the number filled in entry box which is in normal state and inserting the correct number in entry box
            entries[i][j].delete(0, END)
            entries[i][j].insert(0, sudoku[i][j])

            # this statement checks if entry box is in normal state
            if(entries[i][j]['state'] == 'normal'):
                # as this funtion is for solution we need our program to disbale the entry box after solution is shown, also to make the solved or corrected number look different we gonna change the properties of the entry cells (for solution entry cells)
                entries[i][j].config(state="disabled")

                # changing disabled entry box background
                entries[i][j].configure({"disabledbackground": "#c4d8e2"})

                # changing the font colour of text of the solution cell
                entries[i][j].configure({"disabledforeground": "Blue"})


# this funtion calls the solver and the method to dispaly the solution
def solved_command():
    global sudoku
    if (Suduko(sudoku, 0, 0)):
        SolvedUI(sudoku)

#validate row
def isRowValid(row_num):
    return len(set(sudoku[row_num])) == 9
 
#validate column
def isColValid(col_num):
    col = [item[col_num] for item in sudoku]
    return len(set(col)) == 9
 
#validate cell
def isCelValid(cel_row, cel_col):
    vals = sudoku[cel_row][cel_col: cel_col+3]
    vals.extend(sudoku[cel_row+1] [cel_col: cel_col+3])
    vals.extend(sudoku[cel_row+2] [cel_col: cel_col+3])
    return len(set(vals)) == 9
 
#validate sudoku
def validateSudoku():
    for i in range(0,9):
        if not isRowValid(i):
            return False
        if not isColValid(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not isCelValid(i, j):
                return False
    return True


# this funtion is used to check if the user solved sudoku is correct or not
def checkIfBoardIsCorrect():
    if validateSudoku():
        # displaying message in small pop up window
        messagebox.showinfo(title=None, message="Correct! : )")
    else:
        # displaying message in small pop up window
        messagebox.showwarning(title=None, message="Inorrect! : )")


# this funtion changes the sudoku puzzle after the button is clicked
def newGame():
    # accessing the sudoku from the main body of the program as we want the all the changes done here to the main sudoku too
    global sudoku

    for i in range(9):
        for j in range(9):
            # this is to check if the entry boix is disabled
            if(entries[i][j]['state'] == 'disabled'):

                # after program finds entry box in disable state, it will change the background of the cell to the white colour as it was before like it was in normal state
                entries[i][j].configure({"disabledbackground": "white"})

                # this will change the font colour to grey as it was before like it was in normal state
                entries[i][j].configure({"disabledforeground": "Grey"})

                # after changing the properties of the entry boxes, chhanging the disabled state to the normal
                entries[i][j].config(state="normal")

            # deleting the number of normal state box which was not found disabled by upper if statement
            entries[i][j].delete(0, END)

    # using dokusan library to generate the unsolved sudoku
    # using numpy librarry to change the format of returned long string of unsolved sudoku to the 9x9 list of   values (here the items in the list is numbers in string form as dokusan returns the string) and reshape   is makinf 9x9 list
    sudoku = np.array(list(str(generators.random_sudoku(avg_rank=150)))).reshape(9,9)

    # using list comprehension w're chanign the string value to integer values
    sudoku = [[int(sudoku[i][j]) for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if(sudoku[i][j] != 0):
                entries[i][j].insert(0, sudoku[i][j])
                entries[i][j].config(state="disabled")


# this funtion or command is bind to the back button and this will queit the current game and opens up the main screen
def back():
    root.destroy()
    os.startfile('main.py')


# using dokusan library to generate the unsolved sudoku
# using numpy librarry to change the format of returned long string of unsolved sudoku to the 9x9 list of values (here the items in the list is numbers in string form as dokusan returns the string) and reshape is makinf 9x9 list
sudoku = np.array(list(str(generators.random_sudoku(avg_rank=150)))).reshape(9,9)

# using list comprehension w're chanign the string value to integer values
sudoku = [[int(sudoku[i][j]) for i in range(9)] for j in range(9)]

root = Tk()
root.wm_iconbitmap('icon.ico')
root.title("Sudoku Game & Solver")

# setting the size of game window
root.geometry("424x674")
 
# set minimum window size value
root.minsize(424, 674)
 
# set maximum window size value
root.maxsize(424, 674)

# making label frame to set all the sudoku grids in one frame
frame = LabelFrame(root)
frame.grid(padx=2, pady=2,row=0, column=0)

# making blank list to store all the entry widget cells 
entries = []

for i in range(9):
    # this blank list refers to the iteration of rows
    # this list will store rows entry and each list will be appended with 9 entries and after this loop will run for new row 
    entryRow = []
    for j in range(9):
        # here we're calling entry funtion in loop with the properties we need in our window and appending them to the entries list we made earlier 
        curEntry = Entry(frame, width=2, bg = '#c4d8e2', fg = 'Blue', justify = CENTER, font=('Nunito 28'))
        curEntry.grid(row=i, column=j, padx = 0, pady = 0)
        # appending the entry boxes to entryrow list
        entryRow.append(curEntry)
    # appending the entry row list to the main entries list
    entries.append(entryRow)

# entry boxes are ready and in this program we've a funtion which randomy replaces the numbers of blank sudoku (filled with zero earlier) with known cells of sudoku entred by user

# this loop have a statement which checks if the entry box is not filled with zero
# if the cell is any number except zero then the number from the sudoku list will be insetred in the entry box at the same location it was in the sudoku list

for i in range(9):
    for j in range(9):
        if(sudoku[i][j] != 0):
            # inserting the non-zero number from sudoku list to entry box in list entries at same location
            entries[i][j].insert(0, sudoku[i][j])
            # disabling the input by user as the sudoku cell is already known
            # this is done so that the user can not change already known cell
            entries[i][j].config(state="disabled")

# font properties we gonna use in the game window for buttons text
myFont = font.Font(family='Montserrat', size=15, weight='bold')

# making newgame button and passing the command that will be activated after the button click
newButton = Button(root, text="New Game", command = newGame, fg = '#838383')
newButton['font'] = myFont
newButton.grid(row = 9, column = 0, ipadx = 0, ipady = 7, padx = 10, pady = 2, sticky='ew')

# making check button and passing the command that will be activated after the button click
checkButton = Button(root, text="Check", command=checkIfBoardIsCorrect, fg = '#838383')
checkButton['font'] = myFont
checkButton.grid(row = 10, column = 0, ipadx = 0, ipady = 7, padx = 10, pady = 2, sticky='ew')

# making solve button and passing the command that will be activated after the button click
solveButton = Button(root, text="Solution", command=solved_command, fg = '#838383')
solveButton['font'] = myFont
solveButton.grid(row = 11, column = 0, ipadx = 0, ipady = 7, padx = 10, pady = 2, sticky='ew')

# making back button and passing the command that will be activated after the button click
backButton = Button(root, text = 'Back to Menu', command = back, fg = '#838383')
backButton['font'] = myFont
backButton.grid(row = 12, column = 0, ipadx = 0, ipady = 7, padx = 10, pady = 2, sticky='ew')

root.mainloop()
