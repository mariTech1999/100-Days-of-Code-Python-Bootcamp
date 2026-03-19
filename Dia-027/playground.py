def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum*2


print(add(1,2,3,4,5,6,7,8,9,10))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']

my_car = Car(make = "Nissan")
print(my_car.make)