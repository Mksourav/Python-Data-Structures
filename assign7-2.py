# fname = input("Enter file name: ")
# fh = open(fname)
# tfp=0
# afp=0
# c=0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") :
#         continue
#     else:
#         c=c+1
#         fp=line.find('0.8475')
#         fp=float(fp)
#         tfp=afp+fp
# afp=(tfp/c)
# print('Average spam confidence: ',afp)

fname = input("Enter file name: ")
fh = open(fname)
afp=0
tfp=0
c=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        c=c+1
        #print(float(list(line.split())[1]))
        afp+=float(list(line.split())[1])
#print('c',c)
afp=(afp/c)
print('Average spam confidence:',afp)
