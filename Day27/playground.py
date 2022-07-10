from ast import arg


# Unlimited inputs Positional Arguments: since the position in which the arguments are passed matters
def add(*args):
    sum=0
    for num in args:
        sum+=num
    return sum


print(add(10,10))

# **kwargs : Arbitary number of keyword arguments

def calculate(n,**kwargs):
    print(kwargs)
    if kwargs.get('add'):
        n+=kwargs.get('add')
    if kwargs.get('multiply'):
        n*=kwargs.get('multiply')
    print(n)


calculate(2,multiply=20)

class Car:

    def __init__(self,**kw) -> None:
        self.make=kw.get('make')
        self.model=kw.get('model')

my_car=Car(make='Nissan')
print(my_car.model)