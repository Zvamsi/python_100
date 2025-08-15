print("Today's tip calculator")
bill=float(input("Enter the total bill\n"))
tip=float(input("How much you like to give ? 10, 12, 15\n"))
people=int(input("How many people to split the bill ?\n"))
split=(bill+(bill*tip*0.01))/people
print("Each person should pay:",split)
