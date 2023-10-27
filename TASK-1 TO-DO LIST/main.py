# TO DO LIST
from tkinter import*
from tkinter import messagebox

# FUNCTIONS

def addtask():
    
    task = entry.get()

    if task:
        tasklist.insert(END, task)
        entry.delete(0, END)

    else:
        messagebox.showwarning("Warning", "Please Enter A Task.")

def deletetask():

    try:
        #[0] is used to access the first element of the list returned by .curselection()
        selectedtask = tasklist.curselection()[0]
        tasklist.delete(selectedtask)

    except IndexError:
        pass

def markdone():

    try:
        selected_task = tasklist.curselection()[0]
        tasklist.itemconfig(selected_task, {'bg': 'light green'})

    except IndexError:
        pass

def marknotdone():

    try:
        selectedtask = tasklist.curselection()[0]
        tasklist.itemconfig(selectedtask, {'bg': 'light pink'})

    except IndexError:
        pass

# MAIN WINDOW

root = Tk()
root.title("To-Do List")
root.geometry("450x340")
root.wm_iconbitmap("todo.ico")

#HEADING

Label(root, text="TO-DO LIST", font="comicsansms 20 bold", pady=15).grid(row=0, column=2, padx=5, pady=5)

# TASK ENTRY FIELD

entry = Entry(root, width=40)
entry.grid(row=1, column=2, padx=5, pady=5)

# CREATING TASK LIST

#SINGLE − You can only select one line, and you can't drag the mouse.wherever you click button 1, that line is selected.
tasklist = Listbox(root, selectmode=SINGLE, width=40, height=10)
tasklist.grid(row=2, column=2, padx=5, pady=5)

# ADDING SCROLL BAR AS RULES SAY

Scroll = Scrollbar(root, orient=VERTICAL)
tasklist.config(yscrollcommand=Scroll.set)
Scroll.grid(row=2, column=3, sticky="ns")
Scroll.config(command= tasklist.yview)

# CREATING BUTTONS

addbutton = Button(root, text="Add Task", command=addtask)
addbutton.grid(row=1, column=1, padx=5, pady=5)

deletebutton = Button(root, text="Delete Task", command=deletetask)
deletebutton.grid(row=3, column=1, padx=5, pady=5)

donebutton = Button(root, text="Mark As Done", command=markdone)
donebutton.grid(row=3, column=2, padx=5, pady=5)

notdonebutton = Button(root, text="Mark As Not Done", command=marknotdone)
notdonebutton.grid(row=3, column=3, padx=5, pady=5)

# TO EXIT

widget = Button(root, text="EXIT")
widget.grid(row=0, column=1, padx=20, pady=5)
widget.bind('<Double-1>', quit)

root.mainloop()