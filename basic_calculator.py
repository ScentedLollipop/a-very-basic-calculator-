from tkinter import *

root = Tk()

root.title('Calculator')

e = Entry(root)
e.grid(row=0, column=0, columnspan=3)

addition =FALSE
subtraction =FALSE
multiplication =FALSE
division =FALSE


def click(nmbr):
    e.insert(END, nmbr)

def m_click(sign):
    global first_no
    first_no = e.get()
    e.delete(0, END)
    
    if sign == '+':
        global addition
        addition = TRUE
    if sign == '-':
        global subtraction
        subtraction = TRUE
    if sign == '/':
        global division
        division = TRUE
    if sign == 'x':
        global multiplication
        multiplication = TRUE
    
def equal_click():
    second_no = e.get()
    e.delete(0, END)
    if addition:
        ans = int(first_no) + int(second_no)
    if subtraction:
        ans = int(first_no) - int(second_no)
    if multiplication:
        ans = int(first_no) * int(second_no)
    if division:
        ans = int(first_no) / int(second_no)
    e.insert(0, round(int(ans)))

def clear():
    e.delete(0, END)
    global addition
    global subtraction
    global division
    global multiplication
    addition = FALSE
    subtraction = FALSE
    division = FALSE
    multiplication = FALSE

    



b7 = Button(root, text= 7, width=3, command= lambda : click(7))
b7.grid(row=1, column=0)

b8 = Button(root, text= 8, width=3, command= lambda : click(8))
b8.grid(row=1, column=1)

b9 = Button(root, text= 9, width=3, command= lambda : click(9))
b9.grid(row=1, column=2)

b4 = Button(root, text= 4, width=3, command= lambda : click(4))
b4.grid(row=2, column=0)

b5 = Button(root, text= 5, width=3, command= lambda : click(5))
b5.grid(row=2, column=1)

b6 = Button(root, text= 6, width=3, command= lambda : click(6))
b6.grid(row=2, column=2)

b1 = Button(root, text= 1, width=3, command= lambda : click(1))
b1.grid(row=3, column=0)

b2 = Button(root, text= 2, width=3, command= lambda : click(2))
b2.grid(row=3, column=1)

b3 = Button(root, text= 3, width=3, command= lambda : click(3))
b3.grid(row=3, column=2)

bplus = Button(root, text = '+', width=3, command = lambda : m_click('+'))
bplus.grid(row=1, column=4)

bminus = Button(root, text = '-', width=3, command = lambda : m_click('-'))
bminus.grid(row=2, column=4)

bdiv = Button(root, text = '/', width=3, command = lambda : m_click('/'))
bdiv.grid(row=3, column=4)

bx = Button(root, text = 'x', width=3, command = lambda : m_click('x'))
bx.grid(row=4, column=4)

benter = Button(root, text = '=', command = lambda : equal_click(), width= 10)
benter.grid(row=4, column=1, columnspan=2)

bclear = Button(root, text ='Clear', width=3, command = lambda : clear())
bclear.grid(row=4, column=0)





root.mainloop()
