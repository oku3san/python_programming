animal = 'cat'


def f():
    global animal
    animal = 'dog'
    print('after:', animal)


f()
print('global:', animal)
