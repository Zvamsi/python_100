import random

rock='rockpng'
paper='paperpng'
scissor='scissorpng'

print('ROCK PAPER & SCISSOR')
user_choice=int(input("Enter 1 for rock 2 for paper and 3 for scissor"))
computer_choice=random.randint(1,3)
if user_choice==1:
    print(rock)
    print("Computer choose :")
    if computer_choice==2:
        print(paper)
        print("Computer WON")
    elif computer_choice==3:
        print(scissor)
        print("You WON")
    else:
        print("DRAW")
elif user_choice==2:
    print(paper)
    if computer_choice==1:
        print(rock)
        print('You WON')
    elif computer_choice==3:
        print(scissor)
        print("Computer WON")
elif user_choice==3:
    print(scissor)
    if computer_choice==1:
        print(rock)
        print('Computer WON')
    elif computer_choice==2:
        print(paper)
        print("You WON")
else:
    print("Invalid input")