import cv2
import numpy as np
import vehicles
import time
import tkinter 
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import imageio
from PIL import Image, ImageTk
from pynput.mouse import Controller

import os


class Root(Tk):

    def __init__(self):
        # Constructor, Makes version 
        # Args: self = Root
        super(Root, self).__init__()
        self.title("Video File Opener Window")
        self.minsize(600, 400) # Min size of window

        #Graphics window
        self.imageFrame = ttk.Frame(self, width=600, height=500)
        self.imageFrame.grid(row=0, column=0, padx=10, pady=2)

        #Capture video frames
        self.lmain = ttk.Label(self.imageFrame)
        self.lmain.grid(row=4, column=4)

        self.labelFrame = ttk.LabelFrame(self, text = "Open A Video File")
        self.labelFrame.grid(row = 1, column = 0, padx = 10, pady = 20)
        self.button()
        # self.printf()
        self.mouse = Controller()
        global coord
        coord = ''
        self.pt_1 = ttk.Label(self, text = coord)
        self.pt_1.grid(row = 4, column = 6)

        """Create Submit Button"""
        # self.photo = Image.open("C:\Users\mhepel\Pictures\Cars_1.jpeg")
        self.submitButton = Button(self, command=self.buttonClick, text="Submit")
        self.submitButton.grid(row = 4, column = 5)
        
        # self.click()

    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        print('hello')    # do here whatever you want
        global coord
        coord = "f {0}".format(self.mouse.position)
        self.pt_1.configure(text = coord)
        print(coord)
        # self.click()
    



    global vid_x 
    vid_x = 500 # Vid Width
    global vid_y 
    vid_y = 300 # Vid Height

    # def click(self):
      #  global vid_x
       # global vid_y
       # x = vid_x + 100
       # y = vid_y + 100
       # self.vid_button = ttk.Button(self)
       # self.vid_button.config(width = x, height = y)
       # self.vid_button.grid(row = 0, column = 0)
       # print("x: {0}".format(self.mouse.position))

    def button(self):
        # Create Button to open file directory
        self.button = ttk.Button(self.labelFrame, text = "File Browser", command = self.fileDialog)
        self.button.grid(row = 1, column = 1)

    
    

    
    


    def fileDialog(self):
        #Reads file to video and displays video in Gui
        global vid_x
        vid_x = 500 # Vid Width
        global vid_y
        vid_y = 300 # Vid Height
        self.filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select a File") # Read File
        self.label = ttk.Label(self)
        self.label.grid(row = 2, column = 0)
        self.label.configure(text = self.filename) # Display filename
        cap = cv2.VideoCapture(self.filename) # Play video of file

        # while True:
        # Video 
        _, self.frame = cap.read()
        # cv2.imshow('frame', self.frame)
        frame = cv2.flip(self.frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)

        copy_of_image = img.copy() 
        img = copy_of_image.resize((vid_x,vid_y)) # size of video
        imgtk = ImageTk.PhotoImage(image=img)

        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)

        # self.newbut = ttk.Button(self.labelFrame, image = img, command = self.buttonClick)
        # self.newbut.grid(row = 0, column = 0)
        # self.lmain.after(10, self.fileDialog) 

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        cap.release()
        cv2.destroyAllWindows()
        # return self.filename
    
    #def printf(self):
     #   print(self.fileDialog())

if __name__ == '__main__':
    root = Root()
    root.mainloop()