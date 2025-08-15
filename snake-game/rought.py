class Snack:
    juice = 'mango'
    water = 'bisleri' #This variable are associated with class called class variables, can use before or witout declaring objects
    def __init__(self):
        self.cake = 'chocolate'
        self.chips = 'potato' #These variables are associated with object creation so called instance variables and cannot be used without creating variables
    def cook(self):
        print('Cooking starts')
    def end(self):
        print("cooking ends here")

class Bakery(Snack):
    juice='orange'
    def __init__(self):
        super().__init__()
        self.pups='egg'
    def cook(self):
        super().end()
        print("Cooking on going")

print(Bakery.water)
b=Bakery()

print(b.pups)
print(b.cake)
print(b.juice)
b.cook()
