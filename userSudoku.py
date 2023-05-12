from tkinter import *
import tkinter.font as font
from tkinter import messagebox
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


# funtion to replace the ZEROs in sudoku list with user entered values entered in entry boxes
def changeCell():
    # accessing the sudoku from the main body of the program as we want the all the changes done here to the main sudoku too
    global sudoku
    for i in range(9):
        for j in range(9):
            # checking if the entry box is not empty
            if (entries[i][j].get() != ""):
                # replacing the number of sudoku list with user entered value which is fetched from entry box
                sudoku[i][j] = int(entries[i][j].get())

                # after user filled the entry box and clicked the set and solved button then the entry box will be disabled which means now value can not be changed again 
                entries[i][j].config(state="disabled")


# this funtion will clear the previous results and inputs
def clear():
    # accessing the sudoku from the main body of the program as we want the all the changes done here to the main sudoku too
    # basically this resets the whole window, sudoku list, entry list as it was at the very start 
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

    # using list comprehension method making list of size 9x9 
    # list containing list of rows where each row itself is a list of numbers
    # here all the numbers of sudoku set to ZERO
    sudoku = [[0 for i in range(9)] for j in range(9)]


# this funtion is to exit the game and solver window 
def close():
    # this code will pop up the message asking the user if he/she wants to quit
    response = messagebox.askyesno('Exit','Do you want to exit ?')
    if response:
        root.destroy()
    else:
        None

# this funtion or command is bind to the back button and this will queit the current game and opens up the main screen
def back():
    root.destroy()
    os.startfile('main.py')


# using list comprehension method making list of size 9x9 
# list containing list of rows where each row itself is a list of numbers
# here all the numbers of sudoku set to ZERO
sudoku = [[0 for i in range(9)] for j in range(9)]

root = Tk()
root.wm_iconbitmap('icon.ico')
root.title("Sudoku Game & Solver")

# setting the size of solver window
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

# making solve button and passing the command that will be activated after the button click
# lamda method is used to run multiple commands or funtion one after other 
solveButton = Button(root, text="Set & Solve", command=lambda : [changeCell(), solved_command()], fg = '#838383')
solveButton['font'] = myFont
solveButton.grid(row = 9, column = 0, ipadx = 0, ipady = 7, padx = 10, pady = 2, sticky='ew')

# making clear button and passing the command that will be activated after the button click
clearButton = Button(root, text="Clear", command=clear, fg = '#838383')
clearButton['font'] = myFont
clearButton.grid(row = 10, column = 0, ipadx = 0, ipady = 7, padx = 10, pady = 2, sticky='ew')

# making back button and passing the command that will be activated after the button click
backButton = Button(root, text="Back to Menu", command=back, fg = '#838383')
backButton['font'] = myFont
backButton.grid(row = 11, column = 0, ipadx = 0, ipady = 7, padx = 10, pady = 2, sticky='ew')

# making back button and passing the command that will be activated after the button click
closeButton = Button(root, text = 'Close', command = close, fg = '#838383')
closeButton['font'] = myFont
closeButton.grid(row = 12, column = 0, ipadx = 0, ipady = 7, padx = 10, pady = 2, sticky='ew')

root.mainloop()