# n = int(input())
# a = [i for i in list(map(int, input().split()))]

# l = 2 ** n

# f = 0
# fmax = a[f]
# b = l // 2
# bmax = a[b]

# for i in range(l // 2):
#     if fmax < a[i]:
#         fmax = a[i]
#         f = i

# for i in range(l // 2, l):
#     if bmax < a[i]:
#         bmax = a[i]
#         b = i

# if fmax > bmax:
#     print(b + 1)
# else:
#     print(f + 1)

from collections import deque

n = int(input())

a = [-1] + [ *map(int, input().split())]

survive = deque(range(1, 2 ** n + 1))

for _ in range(n - 1):
    winner = deque()
    while survive:
        first = survive.popleft()
        second = survive.popleft()
        if a[first] > a[second]:
            winner.append(first)
        else:
            winner.append(second)
    survive = winner

first = survive.popleft()
second = survive.popleft()

if a[first] > a[second]:
    print(second)
else:
    print(first)










