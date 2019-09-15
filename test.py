#---------Files-----------
# handle=open('mbox.txt','r')

# fhand=open('mbox.txt')

# stuff='Hello\nworld!'
# print (stuff)

# xfile=open('mbox.txt')
# for cheese in xfile:
#     print(cheese)

# fhand=open('mbox.txt')
# count=0
# for line in fhand:
#     count=count+1
# print('Line Count:',count)

# fhand=open('mbox.txt')
# inp=fhand.read()
# print(len(inp))
# print(inp[:20])

# fhand=open('mbox.txt')
# for line in fhand:
#     line=line.rstrip()
#     if line.startswith('Learning'):
#         print(line)

# fhand=open('mbox.txt')
# for line in fhand:
#     line=line.rstrip()
#     if not line.startswith('Learning'):
#             continue
#     print(line)

# fhand=open('mbox.txt')
# for line in fhand:
#     line=line.rstrip()
#     if not 'Learning' in line:
#         continue
#     print(line)

# fname=input('Enter the file name:')
# fhand=open(fname)
# count=0
# for line in fhand:
#     if line.startswith('Learning'):
#         count=count+1
# print('There were',count,'Learning lines in', fname)

# fname=input('Enter the file name:')
# try:
#     fhand=open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()
# count=0
# for line in fhand:
#     if line.startswith('Learning'):
#         count=count+1
# print('There were',count,'Learning lines in', fname)

# fhand=open('mbox.txt')
# inp=fhand.read()
# inp=inp.rstrip()
# print(str.upper(inp))
#
# fname = input("Enter file name: ")
# fh = open(fname)
# inp=fh.read()
# inp=inp.rstrip()
# print(str.upper(inp))

#--------LIST-----------
# print([1, 24, 76])
# print(['red','yellow','blue'])
# print([1,[5, 6], 7])
# print([])
