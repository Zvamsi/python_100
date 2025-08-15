# def life_in_weeks(x):
#     y=(90-x)*52
#     print(f"You have {y} weeks left.")
#
# life_in_weeks(int(input("Enter your age\n")))



def calculate_love_score(name1,name2):
    true = 0
    love=0
    f_name=name1+name2.lower()
    for letter in f_name:
        if letter in ['t','r','u','e']:
            true+=1
        if letter in ['l','o','v','e']:
            love+=1
    print(true,love,sep='')

calculate_love_score(input("Enter your name\n"),input("Enter your partner name\n"))