#Top 10 most common words existed in the file
fhand=open('romeo.txt')
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word, 0)+1
lst=list()
for key, val in counts.items():
    newtup=(val, key)
    lst.append(newtup)
lst=sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)


c={'a':10, 'b':1, 'c':22}
# print(sorted([(v, k) for k,v in c.items()]))
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )
print(tmp)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
