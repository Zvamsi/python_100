def check_leap_year(year):
    #logic
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return False
    return False

if check_leap_year(int(input("Enter a year to check leap year\n"))):
    print("This is leap year")
else:
    print("This is not a leap year")