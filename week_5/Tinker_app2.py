import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk

def welcomeMessage(username):
    #create a Tkinter window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text = f"welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text ="This is Python GUI with Tkinter")
    label_2.pack()


    # Run the Tkinter event loop
    root.mainloop()

def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username == "mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("login","invalid username or password")
#create main window
root = tk.Tk()
root.title("Long form")
root.geometry("500x200")

#Create username label and entry
username_label = tk.Label(root, text="Username: ")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#Create passowrd label
password_Label.pack()
password_entry.pack()
