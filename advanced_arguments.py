# def add(*args):
#     sum=0
#     for num in args:
#         sum+=num
#     print(sum)
#
# add(1,2,3,4,5,6,7)

# def test_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#
# test_kwargs(add=5,mul=6)

class Car():
    def __init__(self,**kw):
        self.color=kw.get('color')
        self.model=kw.get('model')
        self.type=kw.get('type')
        self.info=kw.get('info')

my_car=Car(color='white',model='verna',type='Automatic')
print(my_car.info)