import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title('Noti Box')
app.minsize(500, 300)


def showinfo():
    ask = messagebox.askquestion('info title', 'Do you like coding?')
    if (ask == 'yes'):
        tk.Label(app, text='keep coding').pack()
    else:
        tk.Label(app, text="don't give up").pack()


def showwarning():
    messagebox.showwarning('warning title', 'your app is not responding')


def showerror():
    messagebox.showerror(
        'error title', 'your brain does not support your heart version')


tk.Button(app, text='info', command=showinfo).pack()
tk.Button(app, text='warning', command=showwarning).pack()
tk.Button(app, text='error', command=showerror).pack()


app.mainloop()
