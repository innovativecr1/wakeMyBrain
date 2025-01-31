import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S")
    time_label.config(text=current_time)
    # stroke.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Real-Time Clock")

w, h = round(root.winfo_screenwidth()*0.3), round(root.winfo_screenheight()*0.7)
print(w,h)
root.geometry(f"{w}x{h}")
root.configure(bg="#3b3b3b")

# stroke = tk.Label(root, font=("Helvetica", 60), fg="black", bg="#3b3b3b")
# # stroke.place(relx=0.5, rely=0.5, anchor="center")
# stroke.place(relx=0.5, rely=0.5, anchor="center", x=30, y=30)



time_label = tk.Label(root, font=("Helvetica", 60), text="Nacho", fg="#f0f0f0", bg="#3b3b3b")
time_label.place(relx=0.5, rely=0.5, anchor="center")

# time_label.pack()
update_time()
print("updated")
root.mainloop()
