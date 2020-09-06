print(" --------------------- For Loop-------------------------------")

def sort(List_num):

    for i in range (2):
        mini = i
        for j in range (i,5):
            if List_num [j] < List_num [mini]:
                mini = j

        temp = List_num [i]
        List_num [i]= List_num [mini]
        List_num [mini] = temp

        print(List_num)

List_num = [8,5,2,6,1]
sort(List_num)

print(List_num)



print("_______________ While Loop___________________________")


list =[4,3,1,2,5]
i=0
temp= 0
while i < len(list):
    j = i + 1
    while j < len(list):
        if list[i] > list[j]:
            temp = list[i]
            list[i]=list[j]
            list[j]=temp
        j = j + 1
    i = i + 1
print(list)


