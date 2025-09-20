from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)  # kenarlardan boşluk bırakır

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

# is equal label
is_equal_label = Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)

# Result label
result_label = Label(text="0", font=("Arial", 12))
result_label.grid(column=1, row=1)

# Km label
km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
