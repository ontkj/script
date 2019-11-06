#! /usr/bin/python3

import tkinter as tk

def flash_label_context():
    global v
    v =e.get()
##    print(v)
    label.configure(text=v)
    label.after(100, flash_label_context)

def new_window():
    app=tk.Toplevel(root)
    app.title(v)
    bt10=tk.Button(app, text=v)
    bt10.pack()
    
root=tk.Tk()
v=tk.StringVar()
e=tk.Entry(root)
e.pack()
label=tk.Label(root,text='')
label.pack()

b1=tk.Button(root, text='change label text', command=flash_label_context)
b1.pack()
b2=tk.Button(root, text='create a new window', command=new_window)
b2.pack()

root.mainloop()
