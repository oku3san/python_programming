# def say_something():
#     s = 'hi'
#     return s
#
#
# # say_something()
# # print(type(say_something()))
# #
# # f = say_something
# # f()
#
# result = say_something()
# print(result)

# def what_is_this(color):
#     print(color)
#
#
# what_is_this('red')

# def what_is_this(color):
#     if color == 'red':
#         return 'tomato'
#     elif color == 'green':
#         return 'green pepper'
#     else:
#         return "I don't know"
#
#
# result = what_is_this('a')
# print(result)

# def menu(entree, drink, dessert):
#     print('entree =', entree)
#     print('drink =', drink)
#     print('dessert =', dessert)
#
#
# menu(entree='beef', drink='beer', dessert='ice')

# def sample_func(x, l=[]):
#     l.append(x)
#     return l
#
#
# y = [1, 2, 3]
# r = sample_func(100, y)
# print(r)
#
# y = [1, 2, 3]
# r = sample_func(200, y)
# print(r)
#
# r = sample_func(100)
# print(r)
#
# r = sample_func(100)
# print(r)
#
# def say_something(*args):
#     for arg in args:
#         print(arg)
#
#
# say_something('a', 'b', 2)
#
#
# def menu(entree='beef', drink='wine'):
#     print(entree, drink)
#
#
# menu(entree='beef', drink='coffee')
#
#
# def menu(**kwargs):
#     print(kwargs)
#
#
# menu(entree='beef', drink='coffee')
#
#
# def menu(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
#
#
# menu(entree='beef', drink='coffee')

# def menu(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
#
#
# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'dessert': 'ice',
# }
#
# menu(**d)
