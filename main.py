import tkinter as tk

root = tk.Tk()
root.title("Mg Han Zayar Soe")
root.minsize(500,400)

main = tk.Menu(root)

filem = tk.Menu(main,tearoff=0)

filem.add_command(label='New File')
filem.add_command(label='New Folder')
filem.add_separator()
filem.add_command(label='Open File')
filem.add_separator()
filem.add_command(label='quit',command=exit)

orc = tk.Menu(main,tearoff=0)
orc.add_command(label='file 1')
orc.add_command(label='file 2')
orc.add_command(label='file 3')

filem.add_cascade(label='Open Recent',menu=orc)

orct = tk.Menu(main,tearoff=0)
orct.add_command(label='what ever')

orc.add_cascade(label='orc sub',menu=orct)

main.add_cascade(label='File',menu=filem)

edit = tk.Menu(main,tearoff=0)
edit.add_command(label='undo')
edit.add_command(label='redo')
edit.add_command(label='cut')

main.add_cascade(label='Edit',menu=edit)

root.config(menu=main)

root.mainloop()