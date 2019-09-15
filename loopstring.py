fruit='banana'            #loop through string using while loop
# index=0
# while index<len(fruit):
#     letter=fruit[index]
#     print(index, letter)
#     index=index+1


#loop through string using for loop as a counting program

count=0
for letter in fruit:
    print(letter)
    if letter=='n':
        count=count+1
print('Count of n:',count)
