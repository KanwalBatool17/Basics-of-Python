mylist = [12,3,6,8,2]
lenmylist = len(mylist)

isSorted = False

while not isSorted:
    isSorted = True
    for index in range(0, lenmylist - 1):
        if mylist[index] > mylist[index + 1]:
            isSorted= False
            temp = mylist[index]
            mylist[index] = mylist[index + 1]
            mylist[index + 1] = temp

print(lenmylist)
print(mylist)