# Coffee Machine Data
import time
import math
from time import sleep
from art import logo,cfe_logo
from data import menu,resources,profit



coffee={}
sufficient_resources=True
total=-1
sufficient_balance=False
coffee_served=False

def get_resources():
    print(f'''
Water: {resources['water']}ml
milk: {resources['milk']}ml
coffee: {resources['coffee']}g
money: $ {profit}''')

while True:
    # TODO.1 prompt user by asking "What would you like ? (espresso/latte/cappuccino):"

    print(logo)
    user_input=input("What would you like to have ? (espresso/latte/cappuccino):\n").lower()
    # user_input='espresso'

    # TODO.2 turn off the coffee machine if user input is 0ff

    if user_input=='off':
        exit("Coffe machine is offline for maintenance purpose....!")

    # TODO 3 print report(resources)

    elif user_input=='report':
        get_resources()
        exit('REPORT')

    else:
        coffee=menu[user_input]
        # print(coffee)

    #TODO.4 check the resources for making coffee with coffee requirements

    for keys in coffee['ingredients']:
        if coffee['ingredients'][keys]<=resources[keys]:
            sufficient_resources=sufficient_resources and True
        else:
            sufficient_resources=False
            exit(f"We don't have sufficient {keys} to make a coffee, PLEASE")
    # print(sufficient_resources)

    #TODO.5 Enter the coils like giving names to each coin with dollars and counting.

    if sufficient_resources:
        quarter_coins=int(input("Enter the Quarter coins:"))
        dime_coins=int(input("Enter the dime coins:"))
        nickle_coins=int(input("Enter the nickles coins:"))
        penne_coins=int(input("Enter the pennies coins:"))
        total=round(quarter_coins*0.25+dime_coins*0.10+nickle_coins*0.05+penne_coins*0.01,2)
        print(f"total: {total} coffee price : {coffee['cost']}")

    # TODO.6 Check if money is sufficient to make a coffee else return without coffee

    if total>coffee['cost']:
        sufficient_balance:True
        print(f"{round(total-coffee['cost'],2)} will be your change")
        coffee_served=True
    else:
        coffee_served=False
        exit(f"Insufficient funds, Return {total}")

    # if sufficient_balance==True:
    #     time.sleep(1000)

    #TODO.7 make coffee and return the change

    if coffee_served:
        # print(coffee)
        # print(resources)
        # print(cfe_logo)
        print("☕")
        for keys in coffee['ingredients']:
            resources[keys]=resources[keys]-coffee['ingredients'][keys]
        profit+=coffee['cost']
        get_resources()
        dummy=input(f"Here is your {user_input} enjoy...!")


#TODO.8 REPEAT