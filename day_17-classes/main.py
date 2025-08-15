class User:
    def __init__(self,user_id,user_name):
        print("constructor called")
        self.id=user_id
        self.user_name=user_name
        self.followers=0  #default values given
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1


user_1=User(1,'hello')
user_2=User(2,'hey')

# user_1.id='001'
# user_1.fame='father'

print(user_1.id,user_1.user_name,user_1.followers,user_1.following)
print(user_2.id,user_2.user_name,user_2.followers,user_2.following)

user_1.follow(user_2)

print(user_1.id,user_1.user_name,user_1.followers,user_1.following)
print(user_2.id,user_2.user_name,user_2.followers,user_2.following)

# user_2=User(2,'hey')