# import bisect
# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# k = []
# for _ in range(q):
#     x = int(input())
#     k.append(x)

# dist = [a[0] - 1]
# for i in range(n - 1):
#     dist.append(a[i + 1] - a[i] - 1)

# s = [0] * (n + 1)
# for i in range(n):
#     s[i + 1] = s[i] + dist[i]

# for i in range(q):
#     x = bisect.bisect_left(s[1:], k[i])
#     print(k[i] + x)







import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))
k = []
for _ in range(q):
    x = int(input())
    k.append(x)

na = []
l = []
tmp1 = a[0]
tmp2 = a[0]
con = 1
for i in range(1, n):
    if a[i] - tmp1 == 1:
        con += 1
        tmp1 = a[i]
    else:
        na.append(tmp2)
        l.append(con)
        tmp1 = a[i]
        tmp2 = a[i]
        con = 1

if tmp2 != a[n - 1]:
    na.append(tmp2)
    l.append(con)



ls = [0] * (len(l) + 1)
for i in range(len(l)):
    ls[i + 1] = ls[i] + l[i]

print(na)
print(l)
print(ls)

for i in range(q):
    x = bisect.bisect_right(na, k[i])
    while(True):
        if x + 1 < n:
            if k[i] + ls[x] < na[x + 1]:
                print(k[i] + ls[x])
                break
            else:
                x = bisect.bisect_right(na, k[x])
        else:
            print(k[i] + ls[x])

