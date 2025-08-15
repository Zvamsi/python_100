# noinspection PyUnresolvedReferences
import random
from handman_words import word_list
from hangman_art import title,stages


print(title)
word=random.choice(word_list)
# print(word)
placeholder=''
lives=6



for i in range(len(word)):
    placeholder+="_"
print(placeholder)
finished=False
ref_list=[]
while not finished:
    guess=input("Enter your guess letter\n").lower()
    display=''

# for letter in word:
#     if display=='':
#         for letter in word:
#             if letter==guess:
#                 display+=letter
#             else:
#                 display+="_"
#     else:
#         list_=[]
#         for i in display:
#             list_.append(i)
#         for index,letter in enumerate(word):
#             if letter==guess:
#                 list_[index]=letter
#         display=''
#         for each in list_:
#             display+=each
    if guess in ref_list:
        print("YOU already guessed the", guess)
    for letter in word:
        if guess==letter:
            display+=letter
            ref_list.append(letter)
        elif letter in ref_list:
            display+=letter
        else:
            display+="_"

    if guess not in word:
        lives -= 1
        print(f"sorry the letter {'guess'} is not in choosen word so...")
        print(f"lives :{lives}")
        if lives == 0:
            finished = True
            print("YOU LOSE")
            print(word)
            exit(0)

    print(display)
    print(stages[lives])

    if "_" not in display:
        finished=True
        print("YOU WON")
        exit(0)


