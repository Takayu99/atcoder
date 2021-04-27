n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
counter = 0
dst = [True for i in range(1000)]

for i in range(n):
    for x in range(1000):
        if not(list_a[i] <= x + 1 and list_b[i] >= x + 1):
            dst[x] = False

for i in range(1000):
    if dst[i]:
        counter += 1

print(counter)

"""
完了
"""