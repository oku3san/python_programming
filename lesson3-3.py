# count = 0
# while count < 5:
#     print(count)
#     count += 1

# count = 0
# while True:
#     if count >= 5:
#         break
#     print(count)
#     count += 1

# count = 0
# while True:
#     if count >= 5:
#         break
#     if count == 2:
#         count += 1
#         continue
#     print(count)
#     count += 1

# count = 0
#
# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print('Done')

# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')

# while True:
#     word = input('Enter:')
#     print(type(word))
#     num = int(word)
#     print(type(num))
#     if num == 100:
#         break
#     print('next')

# some_list = [1, 2, 3, 4, 5]
# i = 0
# print(len(some_list))
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# some_list = [1, 2, 3, 4, 5, 9]
# for i in some_list:
#     print(i)

# for _ in range(10):
#     print('hello')

# i = 0
# for i, fruit in enumerate(['apple', 'banana', 'orange']):
#     print(i, fruit)

# days = ['Mon', 'Tue', 'Wed']
# fruits = ['apple', 'banana', 'orange']
# drinks = ['coffee', 'tea', 'beer']
#
# for day, fruit, drink in zip(days, fruits, drinks):
#     print((day, fruit, drink))

d = {
    'x': 100,
    'y': 200
}
for k, v in d.items():
    print(k, ':', v)
