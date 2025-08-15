import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','+','-']

print("Welcome to the pyPassword Generator")
num_letters=int(input("Enter how many letters you want the password to be ?\n"))
num_symbols=int(input("Enter how many symbols you want in it>\n"))
num_numbers=int(input("Enter how many numbers you want in it ?\n"))
total=num_letters+num_symbols+num_numbers
password=""
#
# # i=0
# for choice in range(0,total):
#     # print(i)
#     # i+=1
#
#     major=random.randint(1, 3)
#     # print(major)
#     if major==1:
#         # for letter in range(0,num_letters):
#             _random=random.randint(0,len(letters)-1)
#             #Code to convert letters into upper case with random values capital variable
#             capital=bool(random.randint(0,1))
#             instance=letters[_random]
#             if capital:
#                 instance=instance.upper()
#             password+=instance
#     elif major==2:
#         # for number in range(0,num_numbers):
#             _random=random.randint(0,len(numbers)-1)
#             password+=numbers[_random]
#     elif major==3:
#         # for symbol in range(0,num_symbols):
#             _random=random.randint(0,len(symbols)-1)
#             password+=symbols[_random]
#
# print(password)


#Hard way

password_list=[]
for char in range(0,num_letters):
    password_list.append(random.choice(letters))
for num in range(0,num_numbers):
    password_list.append(random.choice(numbers))
for spcl in range(0,num_symbols):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print("Your password is",password)
