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