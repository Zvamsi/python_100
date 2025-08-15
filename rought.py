# from tkinter import *
#
# window=Tk()
# window.title("TKinter Widgets")
# window.minsize(width=500,height=300)
# window.config(padx=100,pady=100)
#
# # Label
#
# my_label=Label(text='I am a label',font=('Arial',20,'bold'))
# my_label.grid(column=0,row=0)
# my_label.config(padx=10,pady=10)
#
# my_label['text']='Changed text'
# my_label.config(text='text')
#
# # Button
#
# def button_click():
#     print("Hello")
#
# my_button=Button(text='click me',command=button_click)
# my_button.grid(column=0,row=1)
# my_button.config(padx=10,pady=10)
#
#
# # Input
#
# my_input=Entry(width=20)
# my_input.insert(END,string='Some default text')
# my_input.focus()
# my_input.get() #To get text inside the input value
# my_input.grid(column=0,row=2)
# # my_input.config(padx=10,pady=10)
#
#
# # Text Box
#
# my_text_box=Text(height=5,width=35)
# my_text_box.focus()
# my_text_box.insert(END,"Hello this is also some default text for text box.")
# print(my_text_box.get('1.10',END))
# my_text_box.grid(column=1,row=0)
# my_text_box.config(padx=10,pady=10)
#
#
# # Spinbox
#
# def spin_used():
#     print(my_spinbox.get())
#
# my_spinbox=Spinbox(from_=0,to=5,width=10,command=spin_used)
# my_spinbox.grid(column=1,row=1)
# # my_spinbox.config(padx=10,pady=10)
#
#
# # Scale
#
# def scale_used(value):
#     # print(my_scale.get())
#     print(value)
#
# my_scale=Scale(from_=0,to=20, command=scale_used)
# my_scale.grid(column=1,row=2)
# # my_scale.config(padx=10,pady=10)
#
#
# # # Checkbutton
#
# def checkbutton_used():
#     print(checked_state.get())
#
# checked_state=IntVar()
# my_check_button=Checkbutton(text='Is it on ?',variable=checked_state,command=checkbutton_used)
# my_check_button.grid(column=2,row=0)
# my_check_button.config(padx=10,pady=10)
#
#
# # Radiobutton
#
# def radio_button_used():
#     print(radio_state.get())
#
# radio_state=IntVar()
# my_radio_button_1=Radiobutton(text='Mango',value=1,variable=radio_state,command=radio_button_used)
# my_radio_button_2=Radiobutton(text='Orange',value=2,variable=radio_state,command=radio_button_used)
# my_radio_button_1.grid(column=0,row=0)
# my_radio_button_2.grid(column=2,row=1)
# my_radio_button_1.config(padx=10,pady=10)
# my_radio_button_2.config(padx=10,pady=10)
#
#
#
# # Listbox
#
# def listbox_used(event):
#     print(my_listbox.get(my_listbox.curselection()))
#
# my_listbox=Listbox(height=4)
# names=['vamshi','rahul','babel','varshith']
# for name in names:
#     my_listbox.insert(names.index(name),name)
# my_listbox.bind('<<ListboxSelect>>',listbox_used)
# my_listbox.grid(column=2,row=2)
# # my_listbox.config(padx=10,pady=10)
#
#
#
# window.mainloop()

def function():
    inn=input()
    if inn>='0' and inn<='9':
        print(inn)
        function()
    print("HEy")

function()
