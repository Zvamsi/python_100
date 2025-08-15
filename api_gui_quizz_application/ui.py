from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain_obj:QuizBrain):
        self.quiz=quiz_brain_obj
        self.window=Tk()
        self.window.title('GUI QUIzz')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label=Label(text='Score: 0',bg=THEME_COLOR,fg='white',font=('Arial',13,'bold'))
        self.label.config(pady=20)
        self.label.grid(row=0,column=1)

        self.canvas=Canvas(height=250,width=300,bg='white')
        self.question_text=self.canvas.create_text(150,125,width=280,text='Hello',font=('Arial',20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2)

        self.yes_image=PhotoImage(file='./images/true.png')
        self.yes_button=Button(image=self.yes_image,highlightthickness=0,command=self.yes_answer)
        self.yes_button.grid(column=0,row=2,pady=20)

        self.no_image=PhotoImage(file='./images/false.png')
        self.no_button=Button(image=self.no_image,highlightthickness=0,command=self.no_answer)
        self.no_button.grid(column=1,row=2,pady=20)

        self.get_next_question()
        self.window.mainloop()

    def no_answer(self):
        is_right=self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def yes_answer(self):
        is_right=self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.change_color('white')
            self.label.config(text=f'score: {self.quiz.score}')
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f'You reached the end, and score is {self.quiz.score}')
            self.change_color('white')
            self.yes_button.config(state='disabled')
            self.no_button.config(state='disabled')
    def give_feedback(self,is_right):
        if is_right:
            self.change_color('green')
        else:
            self.change_color('red')

        self.window.after(1000,self.get_next_question)


    def change_color(self,color):
        self.canvas.config(bg=color)
