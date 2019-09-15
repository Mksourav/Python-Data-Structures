counts=dict()
fname=input("Enter the file name: ")
fh=open(fname)
for line in fh:
    line=line.rstrip()
    if line.startswith("From") and not line.startswith("From:"):
        word=line.split()
        hr=word[5]
        counts[hr[0:2]]=counts.get(hr[0:2],0)+1
# print("\n",counts.keys())
# print("\n",counts.values())
# print("\n",counts.items())
lst=list()
for key, val in counts.items():
    newtup=(key, val)
    lst.append(newtup)
lst=sorted(lst)
for hour,count in lst[:]:
    print(hour, count)
