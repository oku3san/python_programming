# import sys
# import lesson_package.utils
#
# print(sys.argv)
#
# r = lesson_package.utils.say_twice('hello')
# print(r)

from lesson_package.utils import say_twice

r = say_twice('bbb')
print(r)
