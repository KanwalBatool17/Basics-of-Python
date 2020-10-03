
def selection_sort(list):
    counter1 = 0
    while counter1 < len(list):
        counter2 = counter1 + 1
        while counter2 < len(list):
            if list[counter1] > list[counter2]:
                temp = list[counter1]
                list[counter1] = list[counter2]
                list[counter2] = temp
            counter2 = counter2 + 1
        counter1 = counter1 + 1
    print(list)
selection_sort([1,4,3,5,2])