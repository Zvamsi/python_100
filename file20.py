
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


def calculator():
    print(''' 
     _____________________
    |  _________________  |
    | | Vamshi       0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    ''')
    continue_='y'
    num1=float(input("What's the first number?: \n"))
    while continue_=='y':
        sign=input("Pick an Operation:\n + \n -\n *\n /\n")
        num2=float(input("What's the next number?:\n"))
        dict_={
            "+":add,
            '-':sub,
            '*':mul,
            '/':div,
        }
        result=dict_[sign](num1,num2)
        print(f'{num1} {sign} {num2} = {result}')
        continue_=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if continue_=='y':
            num1=result
        else:
            print("\n"*20)
            calculator()

calculator()




