import tkinter as tk
from time import strftime

from time import strftime

root = tk.Tk()
root.title('time')

def timer():
    string=strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000,timer)

label= tk.Label(    root ,font=('arail',100,'bold'),background='black',foreground='red')
label.pack(anchor='center')
timer()

root.mainloop()

