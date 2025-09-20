from tkinter import *
# this loads everything int he package if you gonna use particular ones not recommended
# normally tkinter.Tk() with this just Tk()
# cant use grid and pack at the same time
def button_clicked():
    print("I got clicked")
    new_text= input.get()# thanks to this code we can use the input
    my_label.config(text=new_text)


window= Tk()
window.title("My First GUI Program")    
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)# it puts a space between your widgets and other things
#LABEL

my_label=Label(text="I'm a label.",font=("Arial",24,"italic"))#creating a label
my_label.config(text="New Text")
# my_label.pack()#displaying the label with otomatic centering expand="True" or side="left"
#PLACE
# my_label.place(x=200,y=100)
my_label.grid(column=0,row=0)# if you use grid you cant have any pack command i guess

#my_label["text"]="New text"  #both of them works

#BUTTONS


button=Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()# to display smth we gotta pack it

new_button= Button(text="New button")
new_button.grid(column=2,row=0)

#ENTRY component
input= Entry(width=10)# creates a input area
print(input.get())
# input.pack()# if you put side="left" or "right" it will pack into that side of gui
input.grid(column=3,row=2)
     



window.mainloop()#this line should be in the end 