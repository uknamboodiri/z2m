def greet(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')

    return wrap_func


@greet
def hello(greeting, emoji=''):
    print(greeting, emoji)


@greet
def bye(greeting):
    print(greeting)


hello('hello', emoji = ':)')
bye('bye')
