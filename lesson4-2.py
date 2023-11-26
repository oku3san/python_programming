# def outer(a, b):
#     def plus(c, d):
#         return c + d
#
#     r = plus(a, b)
#     print(r)
#
#
# outer(1, 2)

# def circle_area_func(pi):
#     def circle_area(radius):
#         return pi * radius * radius
#
#     return circle_area
#
#
# ca1 = circle_area_func(3.14)
# print(ca1)
# print(ca1(10))

# def add_num(a, b):
#     return a + b
#
#
# print('start')
# r = add_num(10, 20)
# print('end')
#
# print(r)

# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#
#     return wrapper
#
#
# def add_num(a, b):
#     return a + b
#
#
# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#
#     return wrapper
#
#
# @print_info
# def add_num(a, b):
#     return a + b
#
#
# r = add_num(10, 20)
# print(r)

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result

    return wrapper


@print_more
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)
