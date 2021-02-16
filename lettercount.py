lst = []


def count(lst):
    letter= 0

    for i in lst:
        if len(i)>5:
            letter+=1
        else:
            pass

    return letter


n = int(input('Enter how many name do you want to enter: '))

for j in range(n):
    x = input('Enter next name: ')
    lst.append(x)

letter = count(lst)
print("No. of name which have greater than 5 letter:",letter)
