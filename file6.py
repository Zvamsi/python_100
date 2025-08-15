import random
friends=["Vamshi",'Rahul','Venu','Rakshith','Ashok','Gopal','Kalam']
print(random.choice(friends))
index=random.randint(0,len(friends)-1)
print("The bill is on",friends[index])