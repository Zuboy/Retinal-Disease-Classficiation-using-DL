# -*- coding: utf-8 -*-
"""
Created on Jan 29 2024 , Aishwaryaraj
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time


global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Retinal disease classification using deep learning")


image2 = Image.open('2.jpg')
image2 = image2.resize((1800, 850))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  
#
label_l1 = tk.Label(root, text="Retinal disease classification using deep learning",font=("Times New Roman", 30, 'bold'),
                    background="brown", fg="white", width=70, height=1)
label_l1.place(x=0, y=0)


def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=160)

button2 = tk.Button(root, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button2.place(x=100, y=240)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="brown", fg="white")
button3.place(x=100, y=330)

root.mainloop()
