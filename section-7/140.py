from functools import reduce

my_list = [1, 2, 3, 4, 5]
my_scores = [85, 54, 35, 26, 0, 90, 112]


# map
def multiply_by_2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulate(acc, item):
    print(acc, item)
    return acc + item


print(list(map(multiply_by_2, my_list)))
# filter
print(list(filter(only_odd, my_list)))
# zip
print(list(zip(my_list, my_scores)))
# reduce

print(reduce(accumulate, my_scores, 0))

# lambda
# lambda param : action(param)

print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_scores, 0))
