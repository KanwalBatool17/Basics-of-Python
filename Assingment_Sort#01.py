mylist = [14,9,3,2,8]
i = 0
temp = 0
while i < len(mylist):
    j = i + 1
    while j < len(mylist):
        if mylist[i] > mylist[j]:
            temp = mylist[i]
            mylist[i] = mylist[j]
            mylist[j] = temp
        j = j + 1
    i = i + 1
print(mylist)