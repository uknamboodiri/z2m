from collections import Counter

my_file = open("./sample.txt")

lines = my_file.readlines()
print(Counter(lines))
print(list('hello'))

my_file.close()
# print(my_file.readline())
# print(my_file.readline())
