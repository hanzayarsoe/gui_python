import tkinter as tk

app = tk.Tk()
app.title('top level')
app.minsize(500,300)

top = None

def toplevel():
    global top
    top = tk.Toplevel(app)
    top.minsize(500,300)
    tk.Label(top,text='Term and Condition').pack()
    tk.Radiobutton(top,text='agree',command=agree).pack()
    tk.Radiobutton(top,text='disagree',command=app.quit).pack()

def agree():
    global top
    top.destroy()
    tk.Label(app,text='you are ready to install now please wait a second...').pack()



btn = tk.Button(app,text='install',padx=5,pady=5,command=toplevel)




btn.pack()
app.mainloop()