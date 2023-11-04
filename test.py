import tkinter as tk

app = tk.Tk()
app.title("Menu")
app.minsize(500,300)

def scaleColor(value):
    if(0<= int(value) <=10):
        scale.config(bg='green')
    elif(10<= int(value) <=20):
        scale.config(bg='blue')
    else:
        scale.config(bg='red')



scale = tk.Scale(app,from_=0,to=30,orient="horizontal",length=300,tickinterval=5,command=scaleColor)
scale.set(5)
scale.pack()
app.mainloop()