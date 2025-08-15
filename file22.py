import math


def is_prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,int(math.sqrt(num))):
            if num==i:
                continue
            if num%i==0:
                return False
        return True


print(is_prime(7919))