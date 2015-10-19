def a(a, *b):
    return a+sum(b)


def b(a, b):
    pass


def c(a, *b, **c):
    pass


#def add(a:int, b:int) -> int:
#    return(a+b)


def foo(bar):
    def inception(*a, **b):
        print('-----')
        print(bar)
        print(a)
        print(b)
    return inception


def test_functions():
    print(a(1, 2, 3, 45, 6))

    print(b(1, b=2))

    print(c(1, 2, c=3))

    #print((add))

    z = {1:['a', 2, 's', 6]}
    w = ['b', 56, 5.4, 3]
    x = foo(z)
    y = foo(w)

    x(12, 4, 4, 5, 6, 4, x=1, y=3, t=5)
    y(647839, y=4)


def print_params(func):
    def print_values(*args, **kwargs):
        print(func.__name__ + '(' +
              ', '.join([str(arg) for arg in args]) +
              (', ' if args and kwargs else '') +
              ', '.join(["{}={}".format(k, v) for k, v in kwargs.items()]) + ')')
        return func(*args, **kwargs)
    return print_values


@print_params
def a(x, y, z=0):
    return x + y + z


def test_decorator():
    print(a(1, 2, 3))


if __name__ == '__main__':
    test_decorator()
