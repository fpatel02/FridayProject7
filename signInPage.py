from tkinter import *
from tkinter import ttk
root = Tk()
Label(root, text = "Welcome to the sign-in page!").pack()

emailLabel = ttk.Label(root, text = "Please enter your email address here").pack()
emailEntry = ttk.Entry(root, text = "Email address: ").pack()

passwordLabel = ttk.Label(root, text = "Please enter your password here").pack()
passwordEntry = ttk.Entry(root, text = "Password: ", show = '*').pack()

confirmPasswordLabel = ttk.Label(root, text = "Confirm your password to sign in").pack()
confirmPasswordEntry = ttk.Entry(root, text = "Confirm password: ", show = '*').pack()

submitButton = ttk.Button(root, text = "Submit").pack()

root.mainloop()