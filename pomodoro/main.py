from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
timer=""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps=1
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    canvas.config(bg=YELLOW)
    tick_label.config(text='',bg=YELLOW)
    timer_label.config(text='Timer',fg=GREEN,bg=YELLOW)
    window.config(bg=YELLOW)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    # while True:
    if reps == 8:
        timer_label.config(text='Long Break',bg=RED)
        tick_label.config(bg=RED)
        canvas.itemconfig(tomato, bg=RED)
        window.config(bg=RED)
        time=long_break_sec
        reps=1
        tick_label.config(text="")
    elif reps % 2 != 0:
        tick_label.config(bg=GREEN)
        timer_label.config(text='Timer',bg=GREEN,fg=YELLOW)
        canvas.config(bg=GREEN)
        window.config(bg=GREEN)
        time=work_sec
    else:
        timer_label.config(text='Short Break',bg=PINK)
        canvas.config(bg=PINK)
        tick_label.config(bg=PINK)
        window.config(bg=PINK)
        time=short_break_sec
        tick_label.config(text=tick_label['text']+'✔')

    count_down(time)
    # reps += 1
    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps,timer
    # count to 00:00
    count_min=count//60
    count_sec=count%60
    if count_min<10:
        count_min='0'+str(count_min)
    if count_sec<10:
        count_sec='0'+str(count_sec)
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count>0:
        timer=window.after(1000, count_down, count-1)
    else:
        reps+=1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)




# Canvas

canvas=Canvas(width=220,height=224,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file='tomato.png')
tomato=canvas.create_image(103,112,image=tomato_image)
timer_text=canvas.create_text(103,130,text='00:00',fill='white',font=(FONT_NAME,30,'bold'))
canvas.grid(column=1,row=1)



# Timer Label
timer_label=Label(text='Timer',fg=GREEN,font=(FONT_NAME,25,'bold'),bg=YELLOW)
timer_label.grid(column=1,row=0)

# start Button
start_button=Button(text='Start',command=start_timer)
start_button.grid(column=0,row=2)

# Reset Button
reset_button=Button(text='stop',command=reset)
reset_button.grid(column=2,row=2)
#Tick
tick_label=Label(text='',fg=GREEN,bg=YELLOW,font=(FONT_NAME,10,'bold'))
tick_label.grid(column=1,row=3)

window.mainloop()