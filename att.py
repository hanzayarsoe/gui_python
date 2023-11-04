import tkinter as tk
from tkinter.font import Font


app = tk.Tk()
app.title('font')
app.minsize(500,300)

font1 = Font(
    family='times',
    size=30,
    underline=True
)

tk.Label(app,text="This is font using font1",font=font1).pack()


app.mainloop()