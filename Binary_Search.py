pos = 0


def search(list, n):
    l = 0
    u = len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos']= mid+1
            return True
        else:
            if list[mid]>n:
                u = mid-1
            else:
                l = mid+1
    return False


list = [3, 4, 5, 8, 9]
n = int(input("Insert number for Searching: "))

if search(list, n):
    print("Found number {} at position {}".format(n, pos))
else:
    print("Not Found")
