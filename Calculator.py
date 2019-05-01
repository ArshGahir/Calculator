from tkinter import*


def btnClick(numbers):          #Displays Numbers when btns are clicked
    global operator
    operator = operator +str(numbers)
    textvariable.set(operator)


def btnEqualsInput():           #Computes displayed numbers
    global operator
    compute = str(eval(operator))
    textvariable.set(compute)
    operator = compute

def btnClearDisplay():          #Clears display
    global operator
    textvariable.set('')
    operator = ''


cal = Tk()                  #Making window
cal.title('Calculator')         #window title
operator = ''                   
textvariable = StringVar()

textDisplay = Entry(cal, font = ('arial',20,'bold'), textvariable = textvariable, bd = 5, insertwidth = 4, bg = 'whitesmoke',
                    highlightbackground = 'whitesmoke', justify = 'right').grid(row = 0, column = 0, columnspan = 10)


#======Top Row========================
btn7 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(7),
                text = '7', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 1, column = 0, sticky = S+N+E+W, rowspan = 1)
btn8 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(8),
                text = '8', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 1, column = 1, sticky = S+N+E+W, rowspan = 1)
btn9 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(9),
                text = '9', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 1, column = 2, sticky = S+N+E+W, rowspan = 1)
addition = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick('+'),
                text = '+', highlightbackground = 'lightgray', bg = 'lightgray', height= 3, width = 6).grid(row = 1, column = 3, sticky = S+N+E+W)
#======Middle Row 1=====================
btn4 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(4),
                text = '4', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 2, column = 0, sticky = S+N+E+W, rowspan = 1)
btn5 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(5),
                text = '5', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 2, column = 1, sticky = S+N+E+W, rowspan = 1)
btn6 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(6),
                text = '6', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 2, column = 2, sticky = S+N+E+W, rowspan = 1)
subtraction = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick('-'),
                text = '-', highlightbackground = 'lightgray', bg = 'lightgray', height= 3, width = 6).grid(row = 2, column = 3, sticky = S+N+E+W)
#=====Middle Row 2=======================
btn1 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(1),
                text = '1', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 3, column = 0, sticky = S+N+E+W, rowspan = 1)
btn2 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(2),
                text = '2', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 3, column = 1, sticky = S+N+E+W, rowspan = 1)
btn3 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(3),
                text = '3', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 3, column = 2, sticky = S+N+E+W, rowspan = 1)
multiplication = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick('*'),
                text = 'x', highlightbackground = 'lightgray', bg = 'lightgray', height= 3, width = 6).grid(row = 3, column = 3, sticky = S+N+E+W)
#=====Bottom Row==========================
btnDecimal = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick('.'),
                text = '.', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 4, column = 0, sticky = S+N+E+W, rowspan = 1)
btn0 = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(0),
                text = '0', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 4, column = 1, sticky = S+N+E+W, rowspan = 1)
btnClear = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick(btnClearDisplay()),
                text = 'C', highlightbackground = 'whitesmoke', bg = 'whitesmoke', height= 3, width = 6).grid(row = 4, column = 2, sticky = S+N+E+W, rowspan = 1)
division = Button(cal, padx = 16, bd = 8, fg = 'black', font = ('arial',20,'bold'), command = lambda:btnClick('/'),
                text = '/', highlightbackground = 'lightgray', bg = 'lightgray', height= 3, width = 6).grid(row = 4, column = 3, sticky = S+N+E+W)
#=====Total=================================
btnTotal = Button(cal, padx = 16, bd = 8, fg = 'white', font = ('arial',20,'bold'), command = lambda:btnClick(btnEqualsInput()),
                text = 'TOTAL', highlightbackground = 'orange', bg = 'orange', height= 3, width = 6).grid(row = 1, column = 4, sticky = S+N+E+W, rowspan = 6)

cal.mainloop()
