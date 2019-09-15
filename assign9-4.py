counts=dict()
fname=input("Enter the file name: ")
fh=open(fname)
for mail in fh:
    mail=mail.rstrip()
    if mail.startswith("From:"):
        word=mail.split()
        counts[word[1]]=counts.get(word[1],0)+1
# print("\n",counts.keys())
# print("\n",counts.values())
# print("\n",counts.items())
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword, bigcount)
