fname = input("Enter file name: ")
fh = open(fname)
for lx in fh:
    ly=lx.strip()
    print(ly.upper())
