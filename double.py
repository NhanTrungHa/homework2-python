def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper


@doubler
def test_funct():
   print("Test text")


test_funct()
