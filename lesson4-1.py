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

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('a')
print(result)
