import tkinter as tk
import random

app = tk.Tk()
app.title('random button')
app.minsize(500,300)




btn = tk.Button(app,text='Raised',relief="raised",command='relif')

btn.pack()

app.mainloop()