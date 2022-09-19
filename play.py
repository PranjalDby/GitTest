from tkinter import ttk
from tokenize import Double
from PlayerSkelton import *
from tkinter import *
root =Tk()
# label1= Label(root,image=bg)
# label1.place(x= 0,y=0)
message = Message(root,foreground='red',text="HELLO WELCOME TO MY SIMPLE MUSIC PLAYER")
message.pack()
play = player(root)
root.mainloop()
