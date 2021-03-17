#Testing out the new project
from tkinter import *
WIDTH = 300
W = 10
H = 5
T = 10
size = 12

root = Tk()
root.title("Calculator")

#Add the Screen
frm_screen = Frame(root)
screen = Text(frm_screen, width=W*3, height=H/4, font=("Helvetica",18))
screen.pack()
frm_screen.grid(column=0, row=0)
#Add the buttons
frm_buttons = Frame(root)
n = 1
while n < T:
    b = Button(frm_buttons, width = W, height = H, text=str(n),font=("Helvetica",size))
    col = int((n-1)%3)
    row = int((n-1)/3)
    b.grid(column=col, row=row)
    n += 1
#add the bottom row of buttons
dot_b = Button(frm_buttons, width=W, height=H, text=".",font=("Helvetica",size))
dot_b.grid(column=0,row=3)
z_b = Button(frm_buttons, width = W, height = H, text="0",font=("Helvetica",size))
z_b.grid(column=1, row=3)
eq_b = Button(frm_buttons, width=W, height=H, text="=",font=("Helvetica",size))
eq_b.grid(column=2,row=3)
frm_buttons.grid(column=0,row=1)

operators = ["+","-","x","/"]
r = 0
c = 3
for i in operators:
    b = Button(frm_buttons, width=W, height=H, text=operators[r],font=("Helvetica",size))
    b.grid(column=c, row=r)
    r += 1




root.mainloop()

