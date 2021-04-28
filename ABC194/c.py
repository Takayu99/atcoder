# n = int(input())
# A = list(map(int, input().split()))

# error = 0

# s = sum(A)
# for i in range(n):
#     error += (n - 1) * A[i] ** 2 - A[i] * (s - A[i])

# print(error)

from collections import Counter

n = int(input())
A = [*map(int, input().split())]

cnt = Counter(A)
ans = 0

for x in range(-200, 201):
    for y in range(x + 1, 201):
        cx = cnt[x]
        cy = cnt[y]
        ans += cx * cy * (x - y) ** 2

print(ans)
