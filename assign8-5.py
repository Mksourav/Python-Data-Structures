fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst=list()
c=0
for line in fh:
    if line.startswith("From:"):
        lst=line.split()
        print(lst[1])
        c=c+1
print("There were", c, "lines in the file with From as the first word")
