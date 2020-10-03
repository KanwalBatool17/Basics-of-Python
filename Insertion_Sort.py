
mylist = [4, 9, 8, 7]
lenghtofList = len(mylist)
rangeoflist = range(1,lenghtofList)
for i in rangeoflist:
    numbertosort = mylist[i]
    while mylist[i-1] > numbertosort and i > 0:
        temp = mylist[i]
        mylist[i] = mylist[i-1]
        mylist[i-1] = temp
        i = i - 1
print(mylist)