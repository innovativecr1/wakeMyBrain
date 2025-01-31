import tkinter as tk
from time import strftime
from tkinter import ttk
import datetime

def update_time():
    current_time = strftime("%H:%M:%S")
    time_label.config(text=current_time)
    # stroke.config(text=current_time)
    if current_time == alarm_entry.get():
        ring_bell()
    root.after(1000, update_time)

def ring_bell():
    print("It's time")

def set_alarm():
    # date_format = '%Y-%m-%d %H:%M:%S'
    
    alarm_time = alarm_entry.get()
    time_data = alarm_time.split(":")
    if len(time_data) == 3:
        print("alarm has been set")
    else:
        print("Check data")    

    print(alarm_time)

root = tk.Tk()
root.title("Real-Time Clock")

w, h = round(root.winfo_screenwidth()*0.3), round(root.winfo_screenheight()*0.7)
print(w,h)
root.geometry(f"{w}x{h}")
root.configure(bg="#3b3b3b")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

style = ttk.Style()
style.configure("TNotebook.Tab", background="#3b3b3b", foreground="#000000", padding=[10, 5])

tab1 = tk.Frame(notebook, bg="#3b3b3b")
notebook.add(tab1, text="Clock")


# stroke = tk.Label(root, font=("Helvetica", 60), fg="black", bg="#3b3b3b")
# # stroke.place(relx=0.5, rely=0.5, anchor="center")
# stroke.place(relx=0.5, rely=0.5, anchor="center", x=30, y=30)


time_label = tk.Label(tab1, font=("Helvetica", 60), text="Nacho", fg="#f0f0f0", bg="#3b3b3b")
time_label.place(relx=0.5, rely=0.5, anchor="center")

tab2 = tk.Frame(notebook, bg="#3b3b3b")
notebook.add(tab2, text="Alarm")

label_tab2 = tk.Label(tab2, text="Set an Alarm:", font=("Helvetica", 20), fg="#f0f0f0", bg="#3b3b3b")
label_tab2.place(relx=0.5, rely=0.3, anchor="center")

alarm_time = tk.StringVar()
alarm_entry = tk.Entry(tab2, textvariable=alarm_time, font=("Helvetica", 14), width=10)
alarm_entry.place(relx=0.5, rely=0.4, anchor="center")

set_alarm_button = tk.Button(tab2, text="Set Alarm (Format: HH:MM:SS)", font=("Helvetica", 14), command=set_alarm)
set_alarm_button.place(relx=0.5, rely=0.5, anchor="center")


# time_label.pack()
update_time()
print("updated")
root.mainloop()
