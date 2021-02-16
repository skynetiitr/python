lst = []


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


n = int(input('Enter how many number do you want to count: '))

for j in range(n):
    x = int(input('Enter next number: '))
    lst.append(x)

print(lst)
even, odd = count(lst)
print('No. of Even: {} and No. of Odd: {}' .format(even,odd))

