import random
try:
    from art24 import logo,vs
    from data24 import data

    def calc_output(obj1,obj2):
        if obj1['follower_count']> obj2['follower_count']:
            return True
        else:
            return False
    a_side=random.choice(data)
    b_side=random.choice(data)
    if a_side==b_side:
        b_side=random.choice(data)

    loose=False
    score=0
    result=-1
    while True:
        try:
            print(logo)
        except SyntaxWarning:
            print("LOGO")
        if score>0 and loose==False:
            print(f"Your score is {score}, continue !")
        if loose:
            print(f"You failed, and your score is {score}")
            exit("You made a wrong choice, Try again")

        print(f"a_side: {a_side}")
        print(f"b_side: {b_side}")
        print(f"Compare A: {a_side['name']}, and he is {a_side['description']}, from {a_side['country']}")
        print(vs)
        print(f"Opponent B: {b_side['name']}, and he is {b_side['description']}, from {b_side['country']}")

        choice=input("Who has more followers ? Type: 'A' or 'B' :\n")
        if choice=='a':
            result=calc_output(a_side,b_side)
        elif choice=='b':
            result=calc_output(b_side,a_side)
        if result==True:
            score=score+1
            a_side=b_side
            b_side=random.choice(data)
        else:
            loose=True
except KeyboardInterrupt as e:
    print("Your program ended because of your finger activities")


