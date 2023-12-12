from tkinter import*

pass

def onclicked():

    lbl.configure(text="Button was clicked!")

window = Tk()

window.title("Welcome to GUI")

window.geometry("350x200")

window.mainloop()

lbl = Label(window, text="Hello", font="Arial")

lbl.grid(column=0, row=0)

window.mainloop()

btn = Button(window, text="Click Me!")

btn.grid(column=1, row=0)

window.mainloop()

