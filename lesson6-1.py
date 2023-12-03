s = 'alkdjflajlabjie'
print(s.capitalize())


class Person(object):
    def __init__(self, name):
        self.name = name
        print('First')
        print(self.name)

    def say_something(self):
        print('hello')


person = Person('Mike')
person.say_something()
