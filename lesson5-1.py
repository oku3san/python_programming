# import sys
# import lesson_package.utils
#
# print(sys.argv)
#
# r = lesson_package.utils.say_twice('hello')
# print(r)

# from lesson_package.utils import say_twice
#
# r = say_twice('bbb')
# print(r)

# from lesson_package import utils
#
# r = utils.say_twice('bbb')
# print(r)
#
# from lesson_package.talk import human
#
# print(human.sing())

from lesson_package.talk import *

print(animal.sing())
print(animal.cry())

print(human.sing())
print(human.cry())
