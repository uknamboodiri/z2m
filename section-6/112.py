class Race():
    Membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('welcome to road rash')

    def shout(self):
        print(self.name)
        print(self.age)


r1 = Race('Dhanya', 18)
r1.shout()
