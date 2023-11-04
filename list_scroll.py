import tkinter as tk

app = tk.Tk()

app.title('Scroll bar')
app.minsize(500,400)

frame = tk.Frame(app)

l = tk.Listbox(frame,width=5,selectbackground='blue',selectmode="extended")

for item in range(100):
    l.insert('end',item)

s = tk.Scrollbar(frame,command=l.yview)

l.config(yscrollcommand=s.set)

l.pack(side='left')
s.pack(side='right',fill='y')

frame.pack()

app.mainloop()