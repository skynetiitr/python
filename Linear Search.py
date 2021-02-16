pos = 0


def search(list, n):
    for i in list:
        globals()['pos'] = pos + 1
        if i == n:
            return True
    return False


list = [4, 8, 3, 9, 5]
n = int(input("Insert number for Searching: "))

if search(list, n):
    print("Found number {} at position {}".format(n, pos))
else:
    print("Not Found")
