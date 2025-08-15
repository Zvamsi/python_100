from rought import Snack

print(Snack.water)
print(Snack.juice)

# print(Snack.cake) #AttributeError: type object 'Snack' has no attribute 'cake'

instance=Snack()

print(instance.cake)
print(instance.chips)

print(instance.juice)
print(instance.water)
