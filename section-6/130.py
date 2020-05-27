class Employee():
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print(f'my employee name {self.name}')


#
class Coach(Employee):
    def __init__(self, name, students):
        self.students = students

    def show(self):
        print(f'my students {self.students}')


class Scientist(Employee):
    def __init__(self, name, topic):
        self.topic = topic

    def show(self):
        print(f'my topic {self.topic}')


class Researcher(Scientist, Coach):
    def __init__(self, name, topic, students):
        Scientist.__init__(self, name, topic)
        Coach.__init__(self, name, 5)
        Employee.__init__(self, name)


me = Researcher('unni', 'ground water', 5)
print(me.name)
print(Researcher.mro())
me.show()
# me.show_coach()
