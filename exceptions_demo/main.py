# try:
#     file=open("a_file.txt",'r')
#     l=[1,2,3,4]
#     print(l[4])
# except FileNotFoundError:
#     file=open('a_file.txt','w')
#     file.write("Something")
# except IndexError as error:
#     print(error)
# else:
#     print(file.read())
# finally:
#     raise ValueError("This is the error i made up")

# height=int(input())
# weight=int(input())
# if height>3:
#     raise ValueError("The height is wayy too high")
# bmi=weight/height**2
# print(bmi)



# l=['apple','orange','pineapple']
# try:
#     item=int(input())
#     i=l[item]
# except IndexError:
#     print("Fruit pie")
# else:
#     print(f'{i} pie')

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]
count=0
for i in facebook_posts:
    try:
        count+=i['Likes']
    except KeyError:
        pass
print(count)


