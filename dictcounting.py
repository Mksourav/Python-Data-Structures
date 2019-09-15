counts=dict()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    words=line.split()

print('words:', words)

print('Counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts', counts)

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print("Biggest word::", bigword, "\nBiggest count::", bigcount)

#Definite loops and dictionaries
count={'chuck' :1, 'fred' :42, 'jan' :100}
for key in count:
    print(key, count[key])

#Retrieving lists of keys and values
jjj={'dude' :1, 'jack' :42, 'jones' :100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#Two iteration variables!
for aaa, bbb in jjj.items():
    print(aaa)
