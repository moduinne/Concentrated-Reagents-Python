#imports
from tkinter import *

#Global constants
W = 10
H = 5
T = 10
size = 12

#init the root
root = Tk()
root.title("Calculator")

#the expression object StringVar()
expression = StringVar()
expression.set("")

#Functions for program
def calculate_expression():
    answer = eval(expression.get().replace("x","*"))
    clear_expression()
    expression.set(answer)
    screen["text"] = expression.get()

def update_expression(item):
    global expression
    global screen
    expression.set(expression.get() + item)
    screen['text'] = expression.get()

def clear_expression():
    expression.set("")
    screen['text'] = expression.get()

#Add the output screen at top
frm_screen = Frame(root)
screen = Label(frm_screen, width=W*3, height=int(H/4), font=("Helvetica",18), text=expression.get())
screen.pack()
frm_screen.grid(column=0, row=0)

#Add the number buttons
frm_buttons = Frame(root)
n = 1
while n < T:
    b = Button(frm_buttons, width = W, height = H, text=str(n),font=("Helvetica",size))
    b['command'] = lambda item = n : update_expression(str(item))
    col = int((n-1)%3)
    row = int((n-1)/3)
    b.grid(column=col, row=row)
    n += 1

#add the second from bottom row buttons
dot_b = Button(frm_buttons, width=W, height=H, text=".",font=("Helvetica",size))
dot_b['command'] = lambda:update_expression(".")
dot_b.grid(column=0,row=3)
zero_b = Button(frm_buttons, width = W, height = H, text="0",font=("Helvetica",size))
zero_b['command'] = lambda: update_expression("0")
zero_b.grid(column=1, row=3)
eq_b = Button(frm_buttons, width=W, height=H, text="=",font=("Helvetica",size), command=calculate_expression)
eq_b.grid(column=2,row=3)
frm_buttons.grid(column=0,row=1)

#add the operator buttons to the right hand column
operators = ["+","-","x","/"]
r = 0
c = 3
for i in operators:
    oper = ""
    b = Button(frm_buttons, width=W, height=H, text=operators[r],font=("Helvetica",size))
    b['command'] = lambda item = operators[r]: update_expression(str(item))
    b.grid(column=c, row=r)
    r += 1

#add the clear button
clear_b = Button(frm_buttons,width=W, height=H, text="C",font=("Helvetica",size),command=clear_expression)
clear_b.grid(column=0,row=4)

#add the brackets buttons
l_brac_b = Button(frm_buttons,width=W, height=H, text="(",font=("Helvetica",size))
l_brac_b['command'] = lambda:update_expression("(")
l_brac_b.grid(column=1, row=4)
r_brac_b = Button(frm_buttons,width=W, height=H, text=")",font=("Helvetica",size))
r_brac_b['command'] = lambda:update_expression(")")
r_brac_b.grid(column=2, row=4)

#Run the main loop
root.mainloop()

