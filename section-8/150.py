from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn()
        end_time = time()
        print(f'{end_time - start_time}s')

    return wrapper


@performance
def loop_through():
    for i in range(1000000000):
        i * 2


loop_through()
