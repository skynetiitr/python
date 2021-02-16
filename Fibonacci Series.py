lst = [0, 1]

n = int(input('How many numbers do you want in Fibonacci Series: '))
if n < 0:
    print('Invalid')
elif n == 0:
    pass
elif n == 1:
    print(lst[0])
else:
    for i in range(n-2):
        c = lst[i]+lst[i+1]
        lst.append(c)

    print(lst)

