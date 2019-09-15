greet=input("Enter the string on which you want to perform the operation::")
# zap=greet.lower()
# print("lower case of the inputted value:",zap)
#
# search=input("Enter the substring you want the find:")
# pos=greet.find(search)
# if pos=='-1':
#     print("substring not found!")
# else:
#     print("substring spotted!")
#     print("So, the position of the substring is ", pos)
#
# old=input("Enter the old substring you want to remove:")
# new=input("Enter the new substring you want to replace on old one:")
# nstr=greet.replace(old,new)
# print("Your new string is ", nstr)


lws=greet.lstrip()
print("String after removing the left whitespace:", lws)
rws=greet.rstrip()
print("String after removing the right whitespace:", rws)
ras=greet.strip()
print("String after removing both left & right whitespace:",ras)
