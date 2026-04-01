import tkinter as tk

def displayMsg():
    name = uname.get()
    msg = "Hi {0}, welcome to IIT!".format(name)
    result.set(msg)

root = tk.Tk()           # create the main window

root.title("My First GUI")
root.geometry("320x150") # width x height (optional)
root.configure(background='green')


#label - CREATE AND PADDING (MIDDLE)
name = tk.Label(root, text="<3 WELCOME TO IIT UNIT! <3", fg='violet')
name.pack()


#label - ask for user name
name = tk.Label(root, text="Please enter your name: ")
name.pack()

#entry for name
uname = tk.StringVar()
name_entry = tk.Entry(root, width=30, textvariable = uname)
name_entry.pack()

#button
clickMe = tk.Button(root, text="Click me!", width=15, background='pink', command=displayMsg)
clickMe.pack()

#entry for result
result = tk.StringVar()
result_entry = tk.Entry(root, width=50, textvariable = result,state="readonly")
result_entry.pack()

root.mainloop()
