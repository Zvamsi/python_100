class QuizBrain:
    def __init__(self,questionn):
        self.question_number=0
        self.question_list=questionn
        self.score=0

    def is_questions_left(self):
        # print(self.question_number)
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        # print(current_question)
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        # print(user_answer)
        # print(correct_answer)
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("YOU are right !")
        else:
            print("you are wrong !")
        print(f"The correct answer is {correct_answer}")
        print(f'Your score is {self.score}/{self.question_number}')
        print('\n')