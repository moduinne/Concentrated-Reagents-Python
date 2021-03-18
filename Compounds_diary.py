from tkinter import *
from datetime import date
import json
root=Tk()
#global constants
frm_bw = 2
frm_rel = RAISED
#Functions######################
def getSampleName():
    global e_title
    global e_book
    global e_page
    print ("DW_AR0" + str(e_book.get()) + "_0" + str(e_page.get()))
#View###########################

#FRAME FOR DETAILS
frm_ents = Frame(root, relief=frm_rel, borderwidth=frm_bw)


Label(frm_ents, text="Global Detail").grid(column=0,row=0)
l_title = Label(frm_ents, text="Title")
l_title.grid(column=0,row=1, padx=5,pady=5)
e_title = Entry(frm_ents)
e_title.grid(column=1,row=1, padx=5,pady=5)

l_book = Label(frm_ents, text="Book")
l_book.grid(column=0,row=2, padx=5,pady=5)
e_book = Entry(frm_ents)
e_book.grid(column=1,row=2, padx=5,pady=5)

l_page = Label(frm_ents, text="Page")
l_page.grid(column=0,row=3, padx=5,pady=5)
e_page = Entry(frm_ents)
e_page.grid(column=1,row=3, padx=5,pady=5)

frm_ents.grid(column=0,row=0, padx=10, pady=10)


#FRAME FOR SUMMARY DESCRIPTION
frm_summary = Frame(root,relief=frm_rel, borderwidth=frm_bw)

Label(frm_summary, text="description/notes").grid(column=0,row=0)

ta_sum = Text(frm_summary, width=25, height=5)
ta_sum.grid(column=0,row=1,padx=5,pady=5)

frm_summary.grid(column=0,row=1,padx=10,pady=10)



#Button(root, text="test",command=getSampleName).grid(column=0, row=1,pady=20)

#Driver##########################
root.mainloop()
