# Fibonacci Numbers


def fib(index):
    a = 0
    b = 1
    for item in range(index):
        yield a
        c = a + b
        b = a
        a = c


print(list(fib(5)))

for i in fib(5):
    print(i)
