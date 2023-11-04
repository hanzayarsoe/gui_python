import tkinter as tk

app = tk.Tk()
app.title('scale widget')
app.minsize(500,400)

def scaleColor(value):
    if(0 <= int(value) <=10):
        scale.config(bg='green')
    elif(11 <= int(value) <=20):
        scale.config(bg='blue')
    else:
        scale.config(bg='red')

scale = tk.Scale(app,tickinterval=5,length=500,from_=0,to=30,orient='horizontal',command=scaleColor)
scale.pack()




app.mainloop()