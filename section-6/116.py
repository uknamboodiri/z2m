class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def runtime_class(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def add(num1, num2):
        return num1 + num2


cat1 = Cat('Dhanya', 18)
print(Cat.add(5, 10))

cat3 = Cat.runtime_class(1, 20)
print(cat3.name)
print(cat3.age)
