def greet(func):
    def wrap_func():
        print('welcome')
        func()

    return wrap_func()


@greet
def hello():
    print('hellooooo')

