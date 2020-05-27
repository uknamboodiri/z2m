from functools import reduce

rows = [0, 1, 2]
layers = [1, 2, 3, 6, 4, 5]
columns = [1, 2, 3, 6, 4, 5]


def multiply_by_2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, layers, 0))
print(list(map(multiply_by_2, layers)))
print(list(filter(only_odd, layers)))

matrix = list(zip(rows, layers, columns))
print(matrix)
a, b, c = matrix
print(a)

# reduce - going to accumulate
