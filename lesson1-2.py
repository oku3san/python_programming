print('Hello, \nHow are you?')

print("=====")
print("""
aaa
bbb
ccc
""")
print("=====")

print("=====")
print("""\
aaa
bbb
ccc\
""")
print("=====")

prefix = 'Py'
print(prefix + 'thon')

s = ('aaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbb')
print(s)

word = "python"
print(word[0], word[-1])
print(word[:4], word[4:])

s = 'My name is Mike. Hi Mike.'
is_start = s.startswith('My')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))

###

print('a is {}'.format('b'))

print('{} {} {}'.format('1', '2', '3'))
print('{2} {1} {0}'.format('1', '2', '3'))
print('My name is {name} {family}. Watashi wa {family} {name}'.format(name='Jun', family='Sakai'))
