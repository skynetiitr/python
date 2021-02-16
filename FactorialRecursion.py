s = 1


def factorial(n):
    global s
    if n == 0:
        return 1
    elif n<0:
        print('Invalid')
    else:
        return n * factorial(n - 1)


n = int(input('Enter a Number: '))
fact = factorial(n)

print('Factorial of {} is {}'.format(n, fact))
