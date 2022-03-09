def func_counter(func):

    # allows for passing of arguments and keyword arguments to wrapper, args is for y
    def wrapper(y):
        wrapper.counter += 1
        func(y)
    wrapper.counter = 0
    return wrapper


@func_counter
def foo(y):
    return y+2**3-34

foo(1)
foo(1)
print(foo.counter)

