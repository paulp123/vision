from main import execute
from tkinter import *
from tkinter.ttk import *

""" 
    purpose: Creates GUI for Traffic analyzer. Passes arguments to main.py

    arguments
    ----------
    file_name: type = String, optimal: must be a video type that cv2.VideoCaputure accepts
    result_name: type = String, optimal: file should not exist, otherwise it overwrites the file
    up_down: type = Integer, optimal: 0 = count cars going down, 1 = count cars going
    up, 2 = count cars going both up and down
    ----------
"""
window = Tk()

window.title("Traffic Analyzer")
 
window.geometry('650x400')
up_down = 0

lbl = Label(window, text="What is the name of the file?")
lbl1 = Label(window, text="What would you like to name the results?")
lbl2 = Label(window, text="Would up like to display cars going down only, up only, or both?")

lbl.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
lbl2.grid(column=0, row=2)

txt = Entry(window,width=10)
txt1 = Entry(window,width=10)

txt.grid(column=1, row=0)
txt1.grid(column=1, row=1)
 


def clicked():    
    file_name = "" + txt.get()
    result_name = "" + txt1.get()
    
    execute(file_name, result_name, up_down)


def clicked1():
""" 
    purpose: sets up_down to 1, which means program will only calculate 
    cars going up
"""
    global up_down
    up_down = 1

    

def clicked2():
""" 
    purpose: sets up_down to 2, which means program will calculate 
    cars going up and down
"""
    global up_down
    up_down = 2

def clicked3():
""" 
    purpose: sets up_down to 0, which means program will only calculate 
    cars going down
"""    
    global up_down
    up_down = 0

    

rad1 = Radiobutton(window,text='Down', value=1, command=clicked3)
rad2 = Radiobutton(window,text='Up', value=2, command=clicked1)
rad3 = Radiobutton(window,text='Both', value=3, command=clicked2)

rad1.grid(column=1, row=2)
rad2.grid(column=2, row=2)
rad3.grid(column=3, row=2)

btn = Button(window, text="Run", command=clicked) 
btn.grid(column=3, row=4)
 
window.mainloop()