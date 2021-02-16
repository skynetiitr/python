from array import *

value = array('i',[])
n = int(input('Enter the length of Array: '))
for i in range (n):
    x = int(input('Enter Next value in Array : '))
    value.append(x)

for e in range (n):
    print(value[e])

y = int(input('Enter search Number : '))

for e in range (n):
    if value[e] == y:
        print('Number Match with Index ',e)
        break
else:
    print('No Number found')
