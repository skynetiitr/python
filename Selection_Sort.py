

def sort(list):
    for i in range(len(list)):
        min_pos = i
        for j in range (i,len(list)):
            if list[min_pos]>list[j]:
                min_pos = j
        temp = list[i]
        list[i] = list[min_pos]
        list[min_pos] = temp


list = [3, 9, 5, 2, 8,-1,55,8,-20]
sort(list)
print(list)

