# Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import Tkinter
import sys
x = Tkinter.Tk()
x.title("Hello World!")
bt = Tkinter.Button(x,text='Exit',width=50,command=x.destroy)
bt.pack()
x.mainloop()

#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
import Tkinter
x = Tkinter.Tk()
def func():
    print("button clicked!")
x = Tkinter.Button(None,text="Hello world",command=func)
x.pack()
x.mainloop()

#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
import Tkinter
from Tkinter import *
x = Tkinter.Tk()
fr = frame()
fr.pack()
root = Tkinter.Tk()
lbl = Label(fr,text="Welcome To Python GUI!")
lbl.pack(side=TOP)
def display():
    global lbl
bt1 = Tkinter.Button(fr,text='Exit',width=50,command=x.destroy)
bt1.pack(side=RIGHT,expand=YES,fill=Y)
bt2 = Tkinter.Button(fr,text='ChangeLabel',width=50,command=display)
bt2.pack(side=LEFT,expand=YES,fill=Y)
root.mainloop()

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
import Tkinter
fr = frame()
fr.pack()
ent = Entry(fr)
ent.pack(side=TOP)
ent.insert(0,"type here..")
ent.focus()
def display():
    print("Rhis is the input: ",ent.get())
bt = Button(fr,text="Hello!",command=display)
bt.pack()
bt.mainloop()