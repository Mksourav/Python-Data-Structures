# purse=dict()
# purse['money']=12
# purse['candy']=3
# purse['tissue']=75
# print(purse)
# ccc=dict()
# ccc['csev']=56
# print(ccc)
# print('csev' in ccc)

counts=dict()
names=['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    # if name not in counts:
    #     counts[name]=1
    # else:
    #     counts[name]=counts[name]+1
    #
    # x=counts.get(name, 0)

    #This is how to combine if & else in one line
    counts[name]=counts.get(name, 0)+1
print(counts)
# print('X=',x)
