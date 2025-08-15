from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# print(question_data)
question_bank=[]

for questions in question_data:
    question=Question(questions['question'],questions['correct_answer'])
    question_bank.append(question)

# print(question_bank[0].text)

quizz=QuizBrain(question_bank)

while quizz.is_questions_left():
    # quizz.is_questions_left()
    quizz.next_question()
print("You Completed quizz !")
print(f"Your score is {quizz.score}/{len(quizz.question_list)}")