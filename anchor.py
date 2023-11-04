import tkinter as tk

app = tk.Tk()
app.title('position')
app.minsize(500,300)

frame = tk.Frame(app).pack()

tk.Label(frame,text="I am here").pack(anchor='e')

app.mainloop()