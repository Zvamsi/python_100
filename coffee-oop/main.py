from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu_=Menu()
while True:
    user_input=input(f"What would you like to have ? {menu_.get_items()}:\n").lower()
    if user_input=='report':
        coffee_maker.report()
        money_machine.report()
        exit("Thanks for caring")
    elif user_input in menu_.get_items():
        item=menu_.find_drink(user_input) #The item stored as MenuItem
    else:
        exit("Sorry try again")

    if coffee_maker.is_resource_sufficient(item):
        # money=money_machine.process_coins()
        if money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)
