def my_for_loop(iterable):
    item = iter(iterable)
    while True:
        try:
            print(next(item))
        except StopIteration:
            break


my_for_loop([1, 2, 3])


# create a range object that returns a iterable
class MyGen:
    current_value = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.last:
            num = self.current_value
            self.current_value += 1
            return num
        raise StopIteration


g = MyGen(0, 100)  # consider MyGen as replacement to range
a = range(0, 100)
for item in a:
    print(item)
