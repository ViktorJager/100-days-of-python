# Unlimited amount of input with *args
# Unlimited positional arguments
def add(*args):
    if args[2]:
        print(args[2])

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.item():
    #   print(key)
    #   print value
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
