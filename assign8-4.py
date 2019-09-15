fname=input("Enter the name: ")
fh=open(fname)
lst=list()
nlst=list()
c=0
for line in fh:
    lst=lst+line.split()
print("List items:\n",lst)
print("List length:",len(lst))
lst.sort()
print("Sorted list items:\n", lst)
for nwlst in range(len(lst)):
    if lst[nwlst-1]!=lst[nwlst]:
        nlst.append(lst[nwlst])
print("Unduplicated list items:\n",nlst)
