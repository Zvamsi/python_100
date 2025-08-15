from tkinter import *
import pandas
import random

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
try:
    data=pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data=pandas.read_csv('data/french_words.csv')
final=data.to_dict(orient='records')
print(len(final))
current_card={}

def both():
    change()
    remove_word()

def remove_word():
    global final
    print(len(final))
    remaining_records=[item for item in final if item!=current_card]
    final=remaining_records
    df=pandas.DataFrame(final)
    df.to_csv('data/words_to_learn.csv',index=False)

def change():
    global current_card,time_delay
    window.after_cancel(time_delay)

    current_card=random.choice(final)
    canvas.itemconfig(main_image,image=card_front)
    canvas.itemconfig(word_line,text=current_card['french'],fill='black')
    canvas.itemconfig(title_line,text='French',fill='black')
    time_delay=window.after(3000,english_translation)

def english_translation():
    canvas.itemconfig(word_line,text=current_card['english'],fill='white')
    canvas.itemconfig(title_line,text='English',fill='white')
    canvas.itemconfig(main_image,image=card_back)

window=Tk()
window.title('Flashy')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
time_delay=window.after(3000,english_translation,)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file='images/card_front.png')
card_back=PhotoImage(file='images/card_back.png')
main_image=canvas.create_image(400,263,image=card_front)
title_line=canvas.create_text(400, 150, text='TITLE',font=('Ariel',40,'italic'))
word_line=canvas.create_text(400, 263, text='WORD',font=('Ariel',60,'bold'))

canvas.grid(column=0,row=0,columnspan=2)

left_button=PhotoImage(file='images/wrong.png')
yes_button=Button(image=left_button,highlightthickness=0,command=change)
yes_button.grid(column=0,row=1)

right_button=PhotoImage(file='images/right.png')
no_button=Button(image=right_button,highlightthickness=0,command=both)
no_button.grid(column=1,row=1)
change()
window.mainloop()
