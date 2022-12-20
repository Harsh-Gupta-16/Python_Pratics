from tkinter import *
from tkinter.ttk import *
from time import strftime

#creating the application main window. 
root = Tk()
root.title('Harsh Clock')


def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

#create widgets 
label = Label(root, font=("Ubuntu",'50'),background = "black", foreground = 'cyan')
#anchor sets the position of text 
label.pack(anchor='center')
time()
#Entering the event main loop 
mainloop()
