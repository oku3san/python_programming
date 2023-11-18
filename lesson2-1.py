l = [1, 20, 30, 50]
print(l)
print(l[0])
print(type(l))
print(list('abcdefg'))

n = [1, 10, 100, 1000, 10000]
print(n)
print(n.pop())
print(n)

###

x = [1, 2, 3]
y = [7, 8, 9]
x.extend(y)
print(x)
print(y)
print(x.index(3))
print(x.count(3))

###

r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 10, 7]
if 5 in r:
    print('exists')
r.sort()
print(r)
r.sort(reverse=True)
print(r)

###
