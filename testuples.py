# x=('a', 'ab', 'abc', 'abcd')
# print(x[0:3])
# print(dir(x))

# l= list()
# print(dir(l))
#
# t= tuple()
# print(dir(t)

# d={'a':10, 'b':1, 'c':22}
# print(d.items())
# print(sorted(d.items()))

#Sort by values instead of key
c={'a':10, 'b':1, 'c':22}
tmp=list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

tmp=sorted(tmp, reverse=True)
print(tmp)
