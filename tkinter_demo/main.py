from tkinter import *

# Creating the Screen

window=Tk()
window.title('GUI Element')
window.minsize(width=500,height=300)

# Label

my_label=Label(text='My name is Vamshi',font=('Arial',30,'bold'))
my_label.pack()

my_label['text']='New text'
my_label.config(text='New Text 2.0')

# Button

def button_clicked():
    my_label.config(text=my_input.get(),font=('Arial',20))
    my_input.delete(0,len(my_input.get()))

my_button=Button(text='Click me',command=button_clicked)
my_button.pack()

# Input

my_input=Entry(width=10)
my_input.pack()
print(my_input.get())

window.mainloop()