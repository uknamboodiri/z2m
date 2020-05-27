def hello(func):
    func()


def greet():
    print('heeelelllloooo')


a = hello(greet)

print(a)
