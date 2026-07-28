from tkinter import *

def button_clicked():
    print("Clicked me!")
    new_text = input.get()
    my_label.config(text=new_text)

#set up window
window =Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="Button 2", command=button_clicked)
button_2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()