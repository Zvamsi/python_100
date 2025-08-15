import random
print('''

  ________                               __  .__                                 ___.                 
 /  _____/ __ __  ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  |  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/ \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
        \/           \/     \/     \/             \/     \/       \/            \/    \/     \/       
 
''')
print("Welcome to the word guessing game \n")
print("Guess the number between 1 and 100")
guess=random.randint(1,100)

def check_guess(choice, live, guess_):
    # print(f'choice {choice} lives {live} guess {guess_}')
    if live==0:
        exit(f"you are out of lives and the guess is {guess}, Better luck Next time")
    if choice==guess_:
        exit("Congratulations, You got it")
    if choice>guess_:
        print("Too High")
        return live-1
    if choice<guess_:
        print('Too Low')
        return live-1
    return None


level=input("Enter the level of difficulty 'easy' or 'hard'\n")
if level=='easy':
    lives=10
else:
    lives=5
print(f"You have {lives} chances to guess the number:")

while True:#lives<0 also applicable but end message won't be visible
    choice=int(input("Guess a number: \n"))
    lives=check_guess(guess_=guess,live=lives,choice=choice)