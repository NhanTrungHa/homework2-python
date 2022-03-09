import time


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Total time ", end - start)

    return wrapper


@calculate_time
def test_funct():
    time.sleep(3)


test_funct()
