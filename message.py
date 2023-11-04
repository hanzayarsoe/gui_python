import tkinter as tk

root = tk.Tk()
root.title("My first tkinter app")
root.minsize(500,300)

tk.Label(root,text="Hi it is label widget",bg='orange').pack()
tk.Message(root,text="Hi it is Message widget",width=400,bg='red').pack()

root.mainloop()