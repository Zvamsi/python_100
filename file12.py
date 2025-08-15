import datetime
# def greet():
#     print("hello")
#     print("Hello again")
#     print("HEllello again and again")
#
# greet()
#
# def greet(name):
#     print(f"Hello {name}")
#     print(f"How are you {name +name}")
#
# greet('vamshi')

def greet(name,location):
    print("Hello",name)
    print("glad you came from",location)
    deadline = datetime.time(12,0,0)
    time=datetime.datetime.now().time()<deadline
    if time:
        print("Good morning")
    else:
        print("Good evening")

greet(location="bangalore",name="vamshi")