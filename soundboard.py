import tkinter as tk
import playsound as p
from tkinter import ttk
from tkinter import *

def playsound(event):
    print(event)
    p.playsound("erm.mp3",block=False)

def playsound1(event):
    print(event)
    p.playsound("skibidi.mp3",block=False)

def playsound2(event):
    print(event)
    p.playsound("gyatt.mp3",block=False)

def playsound3(event):
    print(event)
    p.playsound("fanum.mp3",block=False)

def playsound4(event):
    print(event)
    p.playsound("mog.mp3",block=False)

win = tk.Tk()
win.geometry("470x150")
win.attributes('-topmost',True)


l1 = tk.Label(win,text="press the image to see what sound it makes\ntry to guess what brain rot meme it is :)")

erm = PhotoImage(file="erm.png")
b1 =  tk.Button(win,text="Click to play", image= erm)
b1.bind("<Button>",playsound)

skibidi = PhotoImage(file="skibidi.png")
b2 =  tk.Button(win,text="Click to play", image= skibidi)
b2.bind("<Button>",playsound1)

gyatt = PhotoImage(file="gyatt.png")
b3 =  tk.Button(win,text="Click to play",image=gyatt)
b3.bind("<Button>",playsound2)

fanum = PhotoImage(file="fanum.png")
b4 =  tk.Button(win,text="Click to play", image=fanum)
b4.bind("<Button>",playsound3)

mogging = PhotoImage(file="mog.png")
b5 =  tk.Button(win,text="Click to play", image=mogging)
b5.bind("<Button>",playsound4)


l1.place(x=100, y = 10)
b1.place(x=10, y=50, height=80, width = 80)
b2.place(x=100, y=50, height=80, width = 80)
b3.place(x=190, y=50, height=80, width = 80)
b4.place(x=280, y=50, height=80, width = 80)
b5.place(x=370, y=50, height=80, width = 80)

win.mainloop()