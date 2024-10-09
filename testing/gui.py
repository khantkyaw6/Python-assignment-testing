from tkinter import *


def processOk():
    print("OK button is clicked")


def processCancle():
    print("Cancle button is clicked")


window = Tk()
window.geometry("600x600")
label = Label(window, text="Welcome to Python")
button = Button(window, text="Click Me")

btnOk = Button(window, text="OK", fg="green", command=processOk)
btnCancle = Button(window, text="Cancle", bg="red", command=processCancle)

label.pack()
# button.pack()
btnOk.pack()
btnCancle.pack()


window.mainloop()
