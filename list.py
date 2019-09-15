li=[9, 12, 16, 48, 15, 78, 74]
print(li[1:3])
print(li[:4])
print(li[5:])
print(li[:])
print(len(li))

x=list()
print(type(x))
print(dir(x))

stuff=list()
stuff.append('book')
print(stuff)
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

print(99 in stuff)
print('cookie' not in stuff)
print('dude' in stuff)

fruit='Banana'
fruit[0]='b'
print(fruit)
