from tkinter import *

window=Tk()
# window.minsize(height=80,width=300)
window.title("Mile to km Converter")
window.config(padx=50,pady=20)

# Input

my_input=Entry(width=10)
my_input.grid(column=1,row=0)
my_input.focus()

# Button

def button_click():
    m=float(my_input.get())
    kms=round((m*1.6))
    result.config(text=kms)

calculate=Button(text='Convert',command=button_click)
calculate.grid(column=1,row=3)

# Labels

miles=Label(text='Miles')
miles.grid(column=2,row=0)

is_equal_to=Label(text='is equal to')
is_equal_to.grid(column=0,row=1)

km=Label(text='Km')
km.grid(column=2,row=1)

result=Label(text=0)
result.grid(column=1,row=1)


window.mainloop()