# Creating A Calculator Using Tkinter
from tkinter import*

def click(event):          
    global scvalue    
    
    text = event.widget.cget("text")  

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())     
        else:       
            try:    #EXCEPTION/ERROR HANDLING 
                value = eval(screen.get())   
            except Exception as e:
                print(e)
                value = "Error..."
        
        scvalue.set(value)
        screen.update()

    elif text == "C":    # TO CLEAR
        scvalue.set("")
        screen.update()
        
    else:
        scvalue.set(scvalue.get() + text)    # For example, if the display currently shows "123" and you click the "4" button, this part will result in "123" + "4" becoming "1234."
        screen.update()   
        

root = Tk()   

root.geometry("680x740")
root.maxsize(680,740)
root.title("Calculator")
root.wm_iconbitmap("Cal.ico")
root.config(background="darkgrey")


scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable=scvalue, font= "lucida 70 bold", relief=SUNKEN, background="black", foreground="white")
screen.pack(fill=X, ipadx=8, pady=20, padx=30)   # ipadx is for internal padding


f3 = Frame(root, bg= "black", pady=7)

b3 = Button(f3, text="7", padx=30, pady=18, font= "lucida 34 bold")
b3.pack(side=LEFT, padx=18, pady=5)
b3.bind("<Button-1>", click)                # TO BIND THE BUTTON WITH CLICK EVENT

b3 = Button(f3, text="8", padx=28, pady=18, font= "lucida 34 bold")
b3.pack(side=LEFT, padx=17, pady=5)
b3.bind("<Button-1>", click)

b3 = Button(f3, text="9", padx=28, pady=18, font= "lucida 34 bold")
b3.pack(side=LEFT, padx=15, pady=5)
b3.bind("<Button-1>", click)

b3 = Button(f3, text="%", padx=20, pady=18, font= "lucida 34 bold")
b3.pack(side=LEFT, padx=18, pady=5)
b3.bind("<Button-1>", click)   

f3.pack()


f2 = Frame(root, bg= "black")

b2 = Button(f2, text="4", padx=31, pady=18, font= "lucida 34 bold")
b2.pack(side=LEFT, padx=15, pady=5)
b2.bind("<Button-1>", click)      

b2 = Button(f2, text="5", padx=28, pady=18, font= "lucida 34 bold")
b2.pack(side=LEFT, padx=19, pady=5)
b2.bind("<Button-1>", click)

b2 = Button(f2, text="6", padx=27, pady=18, font= "lucida 34 bold")
b2.pack(side=LEFT, padx=17, pady=5)
b2.bind("<Button-1>", click)

b2 = Button(f2, text="*", padx=28, pady=18, font= "lucida 35 bold")
b2.pack(side=LEFT, padx=18, pady=5)
b2.bind("<Button-1>", click)

f2.pack()


f1 = Frame(root, bg= "black")

b1 = Button(f1, text="1", padx=31, pady=18, font= "lucida 34 bold")
b1.pack(side=LEFT, padx=17, pady=5)
b1.bind("<Button-1>", click)      

b1 = Button(f1, text="2", padx=28, pady=18, font= "lucida 34 bold")
b1.pack(side=LEFT, padx=17, pady=5)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="3", padx=27, pady=18, font= "lucida 34 bold")
b1.pack(side=LEFT, padx=18, pady=5)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="/", padx=33, pady=18, font= "lucida 34 bold")
b1.pack(side=LEFT, padx=16, pady=5)
b1.bind("<Button-1>", click)


f1.pack()


f = Frame(root, bg= "black", pady=7)

b = Button(f, text="0", padx=16, pady=15, font= "lucida 31 bold")
b.pack(side=LEFT, padx=12, pady=5)
b.bind("<Button-1>", click)      

b = Button(f, text=".", padx=18, pady=15, font= "lucida 31 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=12, pady=15, font= "lucida 31 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=14, pady=15, font= "lucida 31 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)      

b = Button(f, text="-", padx=18, pady=15, font= "lucida 31 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=16, pady=15, font= "lucida 31 bold")
b.pack(side=LEFT, padx=12, pady=5)
b.bind("<Button-1>", click)

f.pack()


root.mainloop()