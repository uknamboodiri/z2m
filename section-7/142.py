# list, set and dictionary comprehension
my_list = [char for char in 'hello']

my_list = [char for char in range(0, 100)]

my_list = [char ** 2 for char in range(0, 100)]

my_list = [char ** 2 for char in range(0, 100) if char % 2 != 0]

# print(my_list)

# sets
my_list = {char for char in 'hello'}

my_list = {char ** 2 for char in range(0, 100) if char % 2 != 0}

print(my_list)

# dictionaries
my_dict = {key: value for key, value in enumerate(my_list)}
print(my_dict)

some_chars = ['a', 'e', 't', 's', 'a', 'd', 'c', 'd']

duplicates = list(set([item for item in some_chars if some_chars.count(item) > 1 ]))

print(duplicates)
