print("Welcome to Treasure island.\nYour mission is to find the treasure")
first=input("Enter 'left' or 'right'").lower()
if first=='left':
    second=input("You are in the seashore Enter 'swim' or 'wait'").lower()
    if second=='wait':
        third=input("You saw a boat and 'wave' or 'let it go'").lower()
        if third=='wave':
            fourth=input("The boat looks so suspicious and you 'jump' or 'stay'").lower()
            if fourth=='stay':
                fifth=input("They ask you to have dinner ? 'accept' or 'reject'").lower()
                if fifth=='reject':
                    print("Congratulations, YOU SURVIVED")
                else:
                    print("Poison in the food and Game Over")
            else:
                print("You are eaten by sharks, Game Over")
        else:
            print("You are starved to death, Game Over")
    else:
        print("You were eaten by crocodiles, Game Over")
else:
    print("You fell into dark Hole,Game Over")