from tkinter import *
 
root = Tk()

root.title("MI-265 AttendanceBot")
root.geometry('350x200')

lbl = Label(root, text = "Welcome to GLR MI-265.  Please Sign in")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=0, row=1)

def clicked(event):
    print(event)
    res = "You Wrote " +txt.get()
    lbl.configure(text = res)


root.bind('<Return>', clicked)
root.mainloop()