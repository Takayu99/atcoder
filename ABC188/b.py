n = int(input())
a = [i for i in list(map(int, input().split()))]
b = [i for i in list(map(int, input().split()))]

total = 0

for i in range(n):
    total += a[i] * b[i]

if total == 0:
    print("Yes")
else:
    print("No")