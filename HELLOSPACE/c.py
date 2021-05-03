N = int(input())
A = [tuple(map(int, input().split())) for i in range(N)]

def check(x):
    s = set()
    for a in A:
        s.add(sum(1 << i for i in range(5) if a[i] >= x))
    for x in s:
        for y in s:
            for z in s:
                if x | y | z == 31:
                    return True
    
    return False


left = 0
right = 10 ** 9 + 1

while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)

