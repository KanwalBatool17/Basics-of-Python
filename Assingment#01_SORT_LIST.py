mylist = [8,4,15,9,12]
i = 0

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

