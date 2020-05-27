class Person:
    def __init__(self, is_true):
        self.is_true = not is_true
        return self.is_true


class Teacher(Person):
    def __init__(self, is_true):
        super().__init__(is_true)

    def speak(self):
        print(f'Am I a human? {self.is_true}')


class Scientist(Person):
    def __init__(self, is_true):
        super().__init__(is_true)

    def speak(self):
        print(f'Am I a human? {self.is_true}')


for char in [Teacher(False), Scientist(True)]:
    char.speak()

print(isinstance(char, Person))
