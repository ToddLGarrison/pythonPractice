from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I am a Label", font=("Ariel", 24, "bold"))
my_label.pack(side=("left"))

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()