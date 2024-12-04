def add(*args):
    total = 0
    for n in args:
        total += n
    return print(total)

add(2,3,5,6,1,23,5)

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Tesla", model="Y")
print(my_car.model)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)