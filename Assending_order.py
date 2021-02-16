import array as arr
temp = 0
value = arr.array('i',[4,2,3,10,1,6,8,8,9,12])

for j in range(len(value)):
     for k in range(j+1,len(value)):
         if value[j]>value[k]:
            temp= value[j]
            value[j]= value[k]
            value[k]=temp
            
         else:
             pass


for a in range(len(value)):
    print(value[a])