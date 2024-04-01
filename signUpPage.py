from tkinter import *
from tkinter import ttk
root = Tk()
Label(root, text = "Welcome to the sign-up page!").pack()

emailLabel = ttk.Label(root, text = "Please enter your email address here").pack()
emailEntry = ttk.Entry(root, text = "Email address: ").pack()

passwordLabel = ttk.Label(root, text = "Please enter your password here").pack()
passwordEntry = ttk.Entry(root, text = "Password: ", show = '*').pack()

submitButton = ttk.Button(root, text = "Log in").pack()

root.mainloop()