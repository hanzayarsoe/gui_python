import tkinter as tk

app = tk.Tk()
app.title('label frame')
app.minsize(500, 300)

labelframe = tk.LabelFrame(app, text='Login Form', padx=10, pady=10)

email = tk.Label(labelframe, text='email', padx=10, pady=10)
email_entry = tk.Entry(labelframe)
password = tk.Label(labelframe, text='password', padx=10, pady=10)
password_entry = tk.Entry(labelframe)

email.grid(column=0, row=0)
email_entry.grid(column=1, row=0)
password.grid(column=0, row=1)
password_entry.grid(column=1, row=1)

labelframe.pack()
app.mainloop()
