import time
import os
import sys
import getpass

import tkinter as tk
import threading

from tkinter import *

user = getpass.getuser()
root = Tk()
stop = False

def Quit():
    pass

def timer():
    time.sleep(3)
    os.system("start RusOffice.exe")
    root.destroy()
    sys.exit()

thread = threading.Thread(target=timer)
thread.start()

fon = PhotoImage(file=f"fon.png")
bgLogo = Label(root, image=fon).pack()
root.geometry("500x300")
root.protocol("WM_DELETE_WINDOW", Quit)
root.attributes("-topmost", 1)
root.overrideredirect(1)
x = (root.winfo_screenwidth() - 500) / 2
y = (root.winfo_screenheight() - 300) / 2
root.wm_geometry("+%d+%d" % (x, y))

#command = os.system("python main.py")
#root.after(3000, os.system("python main.py"))
root.mainloop()

