# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3
cat1 = Cat('Dhanya', 16)
cat2 = Cat('Dhanya2', 18)
cat3 = Cat('Dhanya3', 17)


# 2 Create a function that finds the oldest cat
def get_oldest_cat(*args):
    return max(args)


print(f'The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
