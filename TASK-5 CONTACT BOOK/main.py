from tkinter import*
from tkinter import messagebox

# CREATE A LIST TO STORE CONTACT INFORMATION

contacts = [] #list of dictionaries
  
# FUNCTIONS:

def add(): # GET FUNCTION
    name = nameentry.get()
    phone = phoneentry.get()
    email = emailentry.get()
    address = addressentry.get()

    if name and phone:
        contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
        clear_entries()
        update_contact_list()
    
    else:
        messagebox.showwarning("Warning", "Name and Phone Number are required.")

# FUNCTION TO UPDATE THE CONTACT LIST FOR ADD AND DELETE FUNCTIONS

def update_contact_list():
    cont_listbox.delete(0,END)
    for cont in contacts:
        #The END argument ensures that each new entry is added to the end of the listbox.
        cont_listbox.insert(END, f"{cont['Name']} - {cont['Phone']}")


def update():   # SET FUNCTION
    # is used to get the text content of the currently selected item in the Listbox.
    selected_contact = cont_listbox.get(cont_listbox.curselection()) 

    if selected_contact:
        name, phone = selected_contact.split(" - ")
        for cont in contacts:
            if cont['Name']== name and cont['Phone']== phone:
                namevalue.set(cont['Name'])
                phonevalue.set(cont['Phone'])
                emailvalue.set(cont['Email'])
                addressvalue.set(cont['Address'])
                break
def saveupdate():
    selected_contact = cont_listbox.get(cont_listbox.curselection()) 
    nameSel, phoneSel = selected_contact.split(" - ")

    name = nameentry.get()
    phone = phoneentry.get()
    email = emailentry.get()
    address = addressentry.get()

    for cont in contacts:
        if cont['Name'] == nameSel and cont['Phone']== phoneSel:

            cont['Name'] = name
            cont['Phone'] = phone
            cont['Email'] = email
            cont['Address'] = address
            break

    update_contact_list()
    clear_entries()

def delete():
    selected_contact = cont_listbox.get(cont_listbox.curselection())
    if selected_contact:
        name, phone = selected_contact.split("-")
        for cont in contacts:
            if cont['Name']== name and cont['Phone']== phone:
                contacts.remove(cont)
                update_contact_list()
                clear_entries()
                break

def searchc():
    searching = searchvalue.get()
    cont_listbox.delete(0,END)

    for cont in contacts:
        if searching.lower() in cont['Name'].lower() or searching in cont['Phone']:
            cont_listbox.insert(END, f"{cont['Name']} - {cont['Phone']} - {cont['Email']} - {cont['Address']}")

# FUNCTION TO CLEAR ENTRY FIELDS

def clear_entries():
    namevalue.set("")
    phonevalue.set("")
    emailvalue.set("")
    addressvalue.set("")

# MAIN WINDOW
root = Tk()
root.title("Contact Book")
root.geometry("350x500")
root.wm_iconbitmap("contact.ico")

#HEADING

Label(root, text="CONTACT BOOK", font="comicsansms 18 bold", pady=15).grid(row=0, column=2)

# TO EXIT

widget = Button(root, text="EXIT")
widget.grid(row=0, column=1)
widget.bind('<Double-1>', quit)


# TEXT LABELS

name_lb = Label(root, text="NAME")
phone_lb = Label(root, text="PHONE")
email_lb = Label(root, text="EMAIL")
address_lb = Label(root, text="ADDRESS")
search_lb = Label(root, text="SEARCH")

# PACKED TEXT

name_lb.grid(row=1, column=1, padx=5, pady=5)
phone_lb.grid(row=2, column=1, padx=5, pady=5)
email_lb.grid(row=3, column=1, padx=5, pady=5)
address_lb.grid(row=4, column=1, padx=5, pady=5)
search_lb.grid(row=7, column=1, padx=5, pady=5)


# CREATING StringVar() VARIABLES FOR ENTRY DATA

namevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
addressvalue = StringVar()
searchvalue = StringVar()

#ENTRY WIDGETS: ENTRIES FOR OUR CONTACT BOOK

nameentry = Entry(root, textvariable= namevalue)
phoneentry = Entry(root, textvariable= phonevalue)
emailentry = Entry(root, textvariable= emailvalue)
addressentry = Entry(root, textvariable= addressvalue)
searchentry = Entry(root, textvariable= searchvalue)

#PACKING THE ENTRIES

nameentry.grid(row=1,column=2, padx=5, pady=5)
phoneentry.grid(row=2,column=2, padx=5, pady=5)
emailentry.grid(row=3,column=2, padx=5, pady=5)
addressentry.grid(row=4,column=2, padx=5, pady=5)
searchentry.grid(row=7,column=2, padx=5, pady=5)

# CREATE BUTTONS FOR ACTION

b1 = Button(root, text="Add Contact", command=add)
b1.grid(row=5, column=2, padx=5, pady=5)

b2 = Button(root, text="Update Contact", command=update)
b2.grid(row=5, column=1, padx=5, pady=5)

b3 = Button(root, text="Save Updates", command=saveupdate)
b3.grid(row=6, column=1, padx=5, pady=5)

b4 = Button(root, text="Delete Contact", command=delete)
b4.grid(row=6, column=2, padx=5, pady=5)

b5 = Button(root, text="Search Contact", command=searchc)
b5.grid(row=7, column=1, padx=5, pady=5)


# CREATING A LISTBOX TO DISPLAY CONTACTS

cont_listbox = Listbox(root, width=45, height=10)
cont_listbox.grid(rowspan=1, columnspan=3, padx=5, pady=5)

# ADDING SCROLL BAR AS RULES SAY

#"n" - north (the top edge of the widget) & "s" - south(bottom edge)
#sticky="ns" - the scrollbar should expand vertically and stick to both top and bottom of the cell
Scroll = Scrollbar(root, orient=VERTICAL)
cont_listbox.config(yscrollcommand=Scroll.set)
Scroll.grid(row=8, column=3, sticky="ns")
Scroll.config(command=cont_listbox.yview)


# INITIALIZING THE CONTACT LIST
update_contact_list()

root.mainloop()