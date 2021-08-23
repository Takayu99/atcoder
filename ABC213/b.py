n = int(input())
a = list(map(int, input().split()))
if a[0] >= a[1]:
    m, ans = a[0], a[1]
    index1 = 0
    index2 = 1
else:
    m, ans = a[1], a[0]
    index1 = 1
    index2 = 0

for i in range(2, n):
    if a[i] >= ans:
        if a[i] >= m:
            ans = m
            m = a[i]
            index2 = index1
            index1 = i
        else:
            ans = a[i]
            index2 = i
        

print(index2 + 1)
