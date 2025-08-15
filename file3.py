print("This is the pizza deliveries")
size=input("Enter the pizza size S,M,L")
pepperoni=input("Do you want pepperoni Y,N")
extra_cheese=input("Do you want an extra cheese Y,N")

price=0
if size=="S":
    price+=15
elif size=="M":
    price+=20
elif size=='L':
    price+=25
else:
    print("Something went wrong")
if pepperoni=='Y':
    if size=='S':
        price+=2
    else:
        price+=3
if extra_cheese=='Y':
    price+=1

print(f"Your final bill is {price}")