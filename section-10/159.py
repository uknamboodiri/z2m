from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'{end_time - start_time}s')
        return result
    return wrapper


@performance
def loop_with_ranges(num):
    for item in range(num):
        item * 5


@performance
def loop_with_list(num):
    result = []
    for item in range(num):
        result.append(item * 5)


loop_with_ranges(1000)
loop_with_list(1000)
