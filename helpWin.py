from tkinter import *
import tkinter as tk

root = tk.Tk()

# setting title of the window
root.title('Help')

# serring icon of the window
root.wm_iconbitmap('icon.ico')

# here were writing the text we want to show to the user

l_text1 = '''What is a Sudoku Puzzle ?'''
l_text2 = '''In the Sudoku puzzle we need to fill in every empty'''
l_text3 = '''cell with an integer between 1 and 9 in such a way that every'''
l_text4 = '''number appears only once in every row and column.''' 
l_text5 = '''Also there are Nine 3x3 grid which shouldn't have repetion of any number.'''

l_text6 = '''\nInstructions :'''
l_text7 = '''To play sudoku Press "Play"''' 
l_text8 = '''- You can enter digits in the blank cell to complete puzzle by clicking on the cell.'''
l_text9 = '''- After filling all empty cells, press Check button to check your solution.'''
l_text10 = '''- Press "Solution" button to get puzzle auto solved.'''
l_text11 = '''- Press "Back to menu" to return to the main screen.'''

l_text12 = '''\nWant a Solution of your Sudoku!'''
l_text13 = '''Press the button'''
l_text14 = '''- Fill the know cells fo the Sudoku by clicking on the cell.'''
l_text15 = '''- Press Set & Solve to feed the sudoku and get the required solution.'''
l_text16 = '''- Want to solve another?'''
l_text17 = '''  Press "Clear" button and you are good to go with another puzzle you want to get solved.'''


# calling label funtion to display the text to the user
# using row and column parameters to specify where we want the text in window

helpLabel1 = Label(root, text = l_text1, font=('Montserrat', 13)).grid(row = 0, column = 0, sticky=W)
helpLabel2 = Label(root, text = l_text2, font=('Montserrat', 13)).grid(row = 1, column = 0, sticky=W)
helpLabel3 = Label(root, text = l_text3, font=('Montserrat', 13)).grid(row = 2, column = 0, sticky=W)
helpLabel4 = Label(root, text = l_text4, font=('Montserrat', 13)).grid(row = 3, column = 0, sticky=W)
helpLabel5 = Label(root, text = l_text5, font=('Montserrat', 13)).grid(row = 4, column = 0, sticky=W)
helpLabel6 = Label(root, text = l_text6, font=('Montserrat', 13)).grid(row = 5, column = 0, sticky=W)
helpLabel7 = Label(root, text = l_text7, font=('Montserrat', 13)).grid(row = 6, column = 0, sticky=W)
helpLabel8 = Label(root, text = l_text8, font=('Montserrat', 13)).grid(row = 7, column = 0, sticky=W)
helpLabel9 = Label(root, text = l_text9, font=('Montserrat', 13)).grid(row = 8, column = 0, sticky=W)
helpLabel10 = Label(root, text = l_text10, font=('Montserrat', 13)).grid(row = 9, column = 0, sticky=W)
helpLabel11 = Label(root, text = l_text11, font=('Montserrat', 13)).grid(row = 10, column = 0, sticky=W)
helpLabel12 = Label(root, text = l_text12, font=('Montserrat', 13)).grid(row = 11, column = 0, sticky=W)
helpLabel13 = Label(root, text = l_text13, font=('Montserrat', 13)).grid(row = 12, column = 0, sticky=W)
helpLabel14 = Label(root, text = l_text14, font=('Montserrat', 13)).grid(row = 13, column = 0, sticky=W)
helpLabel15 = Label(root, text = l_text15, font=('Montserrat', 13)).grid(row = 14, column = 0, sticky=W)
helpLabel16 = Label(root, text = l_text16, font=('Montserrat', 13)).grid(row = 15, column = 0, sticky=W)
helpLabel17 = Label(root, text = l_text17, font=('Montserrat', 13)).grid(row = 16, column = 0, sticky=W)

root.mainloop()