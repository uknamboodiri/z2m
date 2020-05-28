result = []
for item in range(100):
    result.append(item)


# generators
def generator_range(num):
    for item in range(num):
        yield item


g = generator_range(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
