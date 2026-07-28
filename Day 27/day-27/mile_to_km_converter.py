from tkinter import *

#convert
def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.configure(text=f"{km}")

#set up window
window = Tk()
window.title("Miles to Kilometers")
window.configure(padx=20, pady=20)

#create widgets
#create input box for miles
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#labels/text
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#calculate button
calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()