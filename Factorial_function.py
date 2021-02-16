def factorial(n):
    s = 1
    if n < 0:
        print('Not Define')
    else:
        for i in range(n, 0, -1):
            s = s * i
    return s


n = int(input('Enter a Number: '))

fact = factorial(n)

print('Factorial of {} is {}' .format(n,fact))
