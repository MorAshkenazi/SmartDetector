# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:27:53 2019

@author: morac
"""

import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
from PIL import ImageTk, Image

#---------------Controllers------------
    
def mainScreenController():
    
    frame = tk.Frame(root, bg='#336699')
    frame.place(relwidth=1, relheight=1)
    
    welcomeLabel = tk.Label(frame, text="Welcome!", bg='#336699', fg='#b4cde4', font=40)
    welcomeLabel.config(font=("Buxton Sketch", 44))
    welcomeLabel.grid(row=7, column=50)
    
    #jourLabel = tk.Label(frame, text="Start your journey now!", bg='#336699', fg='white', font=40)
    #jourLabel.config(font=("Buxton Sketch", 20))
    #jourLabel.grid(row=31, column=140)
    
    detectButton = tk.Button(frame, text="Detect", bg='#d9e6f2', fg='black', bd=1, font=50, command=detectButtonPressed)
    detectButton.config(font=("Segoe UI Semibold", 18))
    detectButton.place(relx=0.4, rely=0.6,  relwidth=0.2, relheight=0.1)
    
    infoButton = tk.Button(frame, text="Info", bg='#d9e6f2', fg='black', bd=0.5, font=40, command=infoScreenController)
    infoButton.config(font=("Segoe UI Semibold", 12))
    infoButton.place(relx=0.45, rely=0.8,  relwidth=0.09, relheight=0.09)
    
    img = ImageTk.PhotoImage(Image.open("C:/Users/morac/Desktop/logo-new.png"))
    imglabel = tk.Label(frame, image=img, bg='#336699').grid(row=6, column=10)           
    root.mainloop()
    
def infoScreenController():
    frame = tk.Frame(root, bg='#336699')
    frame.place(relwidth=1, relheight=1)
    
    titleLabel = tk.Label(frame, text="INFO", bg='#336699', fg='#b4cde4', font=40)
    titleLabel.config(font=("Calibri", 36))
    titleLabel.grid(row=2, column=250)
    
    textLabel = tk.Label(frame, text="Amit & Mor - Final Project", bg='#336699', fg='white', font=40)
    textLabel.config(font=("Buxton Sketch", 20))
    textLabel.grid(row=31, column=140)
     
    backButton = tk.Button(frame, text="Back", bg='#d9e6f2', fg='black', bd=1, font=50, command=mainScreenController)
    backButton.config(font=("Segoe UI Semibold", 14))
    backButton.place(relx=0.05, rely=0.85,  relwidth=0.1, relheight=0.1)
    
    root.mainloop()

def chooseSourceScreenController():
    v = tk.StringVar()
    frame = tk.Frame(root, bg='#336699')
    frame.place(relwidth=1, relheight=1)
    
    titleLabel = tk.Label(frame, text="DETECTION", bg='#336699', fg='#b4cde4', font=40)
    titleLabel.config(font=("Berlin Sans FB", 32))
    titleLabel.grid(row=2, column=30)
    
    liveFeedRadioButton = tk.Radiobutton(frame, text="Live Feed", bg='#336699', fg='white', activebackground='#336699', selectcolor='black', variable=v, value=1, command=liveFeedChosen(frame))
    liveFeedRadioButton.config(font=("Segoe UI Semibold", 22))                    
    liveFeedRadioButton.grid(row=10, column=30)
    
    camerasComboBox = ttk.Combobox(frame, values=["Front Camera", "USB Camera"], state='readonly')
    camerasComboBox.set('Front Camera')
    camerasComboBox.config(font=("Segoe UI Semibold", 12))  
    camerasComboBox.grid(row=10, column=31)
    
    videoFileRadioButton = tk.Radiobutton(frame, text="Video File", bg='#336699', fg='white', activebackground='#336699', selectcolor='black', variable=v, value=2, command=liveFeedChosen(frame))
    videoFileRadioButton.config(font=("Segoe UI Semibold", 22))                    
    videoFileRadioButton.grid(row=13, column=30)
    
    pathLabel = tk.Label(frame, text="Path:", bg='#336699', fg='#b4cde4')
    pathLabel.config(font=("Segoe UI Semibold", 12))
    pathLabel.grid(row=14, column=30)
    
    textBox = tk.Text(frame, height=1.3, width=33)
    textBox.grid(row=14, column=31)
    
    browseButton = tk.Button(frame, text="Browse", bg='#d9e6f2', fg='black', bd=1, font=50, command=browsefunc)
    browseButton.config(font=("Segoe UI Semibold", 12))
    browseButton.place(relx=0.85, rely=0.40,  relwidth=0.12, relheight=0.08)
     
    backButton = tk.Button(frame, text="Back", bg='#d9e6f2', fg='black', bd=1, font=50, command=mainScreenController)
    backButton.config(font=("Segoe UI Semibold", 14))
    backButton.place(relx=0.05, rely=0.85,  relwidth=0.1, relheight=0.1)
    
    startButton = tk.Button(frame, text="Start", bg='#d9e6f2', fg='black', bd=1, font=50, command=startButtonPressed)
    startButton.config(font=("Segoe UI Semibold", 14))
    startButton.place(relx=0.45, rely=0.85,  relwidth=0.2, relheight=0.1)
    #img = ImageTk.PhotoImage(Image.open("C:/Users/morac/Desktop/infoIcon.png"))
    #imglabel = tk.Label(frame, image=img, bg='#336699').grid(row=1, column=70)           
    root.mainloop()

def detectionScreenController():
    frame = tk.Frame(root, bg='#336699')
    frame.place(relwidth=1, relheight=1)
    
    img = ImageTk.PhotoImage(Image.open("C:/Users/morac/Desktop/logo-new.png"))
    imglabel = tk.Label(frame, image=img, bg='#336699').grid(row=6, column=10)
    
    textLabel = tk.Label(frame, text="Detected video right here", bg='#336699', fg='white', font=40)
    textLabel.config(font=("Buxton Sketch", 20))
    textLabel.grid(row=31, column=140)
    
    captureButton = tk.Button(frame, text="Capture", bg='#d9e6f2', fg='black', bd=1, font=50, state='disabled', command=mainScreenController)
    captureButton.config(font=("Segoe UI Semibold", 14))
    captureButton.place(relx=0.65, rely=0.85,  relwidth=0.15, relheight=0.1)
    
    backButton = tk.Button(frame, text="Back", bg='#d9e6f2', fg='black', bd=1, font=50, command=chooseSourceScreenController)
    backButton.config(font=("Segoe UI Semibold", 14))
    backButton.place(relx=0.05, rely=0.85,  relwidth=0.1, relheight=0.1)
    
    pauseButton = tk.Button(frame, text="Pause", bg='#d9e6f2', fg='black', bd=1, font=50, command=popupMsg)
    pauseButton.config(font=("Segoe UI Semibold", 14))
    pauseButton.place(relx=0.45, rely=0.85,  relwidth=0.15, relheight=0.1)
    
    root.mainloop()
    
def popupMsg():
    msg = "Are you sure?"
    popup = tk.Tk()
    popup.wm_title("Smart Detector")
    popup.geometry("200x100+300+300")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    b1 = tk.Button(popup, text = "Ok", command = popup.destroy)
    b1.pack()
    popup.mainloop()
    

    
# ---------------buttonsAction--------------

def detectButtonPressed():
    print("Detect Button has Pressed!")
    chooseSourceScreenController()

def liveFeedChosen(frame):
    print("live Feed Button was chosen!")
    
def startButtonPressed():
    print("start Button has Pressed!")
    detectionScreenController()
    
def browsefunc():
    filename = filedialog.askopenfilename()
    print(filename)
   


HEIGHT = 400
WIDTH = 600
root = tk.Tk()
root.title("SmartDetector")

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

mainScreenController()
    
root.mainloop()