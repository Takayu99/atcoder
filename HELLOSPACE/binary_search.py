def binary_search(a, key):
    left = 0
    right = len(a) - 1

    while right >= left:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid - 1
        elif a[mid] < key:
            left = mid + 1


def lower_bound(a, key):

    def isOK(index):
        if(a[index] >= key):
            return True
        else:
            return False
    
    if a[0] >= key:
        return 0
    if a[-1] < key:
        return -1

    left = 0
    right = len(a) - 1

    while (right - left > 1):
        mid = (left + right) // 2
        if isOK(mid):
            right = mid
        else:
            left = mid
    
    return right
    

a = [1, 3, 4, 5, 7, 8, 9]

# index = binary_search(a, 2)
index = lower_bound(a, 10)
print(index)