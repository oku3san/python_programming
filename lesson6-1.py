# s = 'alkdjflajlabjie'
# print(s.capitalize())
#
#
# class Person(object):
#     def __init__(self, name='Default'):
#         self.name = name
#         print('First')
#         print(self.name)
#
#     def say_something(self):
#         print('hello')
#
#
# person = Person()
# person.say_something()

class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(100)

    def run(self, num):
        print('run' * num)


person = Person('Mike')
person.say_something()
