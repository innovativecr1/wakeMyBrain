# # import tkinter as tk
# # import datetime

# # currentTime = datetime.datetime.now().time().strftime("%H %M")

# # def setTime():
# #     text_var.set(currentTime)

# # root = tk.Tk()

# # text_var = tk.StringVar()

# # text_var.set("Old Text")

# # root.configure(background="#000000")
# # w, h = root.winfo_screenwidth(), root.winfo_screenheight()


# # label = tk.Label(root, textvariable=text_var)
# # label.grid(column=0, row=0)


# # quit_button = tk.Button(root, text="Quit", command=root.destroy)
# # quit_button.grid(column=0, row=1)


# # change_button = tk.Button(root, text="Change", command=setTime)
# # change_button.grid(column=0, row=2)


# # root.mainloop()



# import tkinter as tk					 
# from tkinter import ttk 


# root = tk.Tk() 
# root.title("Tab Widget") 
# tabControl = ttk.Notebook(root) 

# tab1 = ttk.Frame(tabControl) 
# tab2 = ttk.Frame(tabControl) 

# tabControl.add(tab1, text ='Tab 1') 
# tabControl.add(tab2, text ='Tab 2') 
# tabControl.pack(expand = 1, fill ="both") 

# ttk.Label(tab1, text ="tab 1").grid(column = 0, row = 0, padx = 30, pady = 30) 
# ttk.Label(tab2, text ="tab 2").grid(column = 0, row = 0, padx = 30, pady = 30) 

# root.mainloop() 

from datetime import datetime

date_str = '14:30:00'
date_format = '%H:%M:%S'
date_obj = datetime.strptime(date_str, date_format)
print(date_obj)
