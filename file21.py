import random
from operator import indexOf

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def add_card():
    random_card=random.choice(cards)
    return random_card

def compare(user_list,computer_list):
    if sum(user_list)==sum(computer_list):
        print("Draw")
    if sum(user_list) == 21:
        print('User Moves', user_list, sum(user_list))
        print("You win 😎")
        # print('\n'*20)
        continue_ = 'no'
        black_jack()
    if sum(user_list) > 21:
        print('User Moves', user_list, sum(user_list))
        print("you Loose 🤯")
        # print('\n'*20)
        continue_ = 'no'
        black_jack()
    # if sum(user_list) < 21:
    #     print('User moves', user_list, sum(user_list))
    if sum(computer_list) == 21:
        print("Computer win with JACKPOT")
        black_jack()
    if sum(computer_list)>21:
        if 11 in computer_list:
            computer_list.remove(11)
            computer_list.append(1)
        print("computer loose")
        black_jack()
    if sum(user_list)<sum(computer_list):
        print("Computer is won")

def black_jack():
    start_='yes'
    start_=input("Enter 'yes' to play black Jack or enter 'no' to exit\n").lower()
    user_list=[]
    computer_list=[]
    if start_=='yes':
        print('''''')
        user_list.append(add_card())
        user_list.append(add_card())
        computer_list.append(add_card())
        if sum(user_list)==21:
            print("BLACK JACK")
            black_jack()
        print('User moves',user_list,sum(user_list),'Computer Moves',computer_list,sum(computer_list))
        continue_=input("Type 'yes' to pick an extra card or type 'no' to hand it to other player:\n")
        while continue_=='yes':
            user_list.append(add_card())
            if sum(user_list) > 21:
                if 11 in user_list:
                    user_list.remove(11)
                    user_list.append(1)
            compare(user_list,computer_list)
            print(user_list,sum(user_list))
           
            continue_ = input("Type 'yes' to pick an extra card or type 'no' to hand it to other player:\n")
        while continue_=='no':
            computer_list.append(add_card())
            print('Computer moves',computer_list,sum(computer_list))
            if sum(computer_list) > 21:
                if 11 in computer_list:
                    computer_list.remove(11)
                    computer_list.append(1)
            compare(user_list, computer_list)

            if sum(computer_list)<17:
                computer_list.append(add_card())



black_jack()