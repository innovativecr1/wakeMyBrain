import tkinter as tk
import datetime

currentTime = datetime.datetime.now().time().strftime("%H %M")

def setTime():
    text_var.set(currentTime)

root = tk.Tk()

text_var = tk.StringVar()

text_var.set("Old Text")

root.configure(background="#000000")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()


label = tk.Label(root, textvariable=text_var)
label.grid(column=0, row=0)


quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.grid(column=0, row=1)


change_button = tk.Button(root, text="Change", command=setTime)
change_button.grid(column=0, row=2)


root.mainloop()