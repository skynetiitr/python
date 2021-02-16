
try:
    print("Resource Open")
    a = int(input("Insert a: "))
    b = int(input("Insert b: "))
    print(a / b)

except ZeroDivisionError:
    print("Can't Divide by Zero")

except ValueError:
    print("Invalid Input")

finally:
    print("Resource Close")

print("Bye")

