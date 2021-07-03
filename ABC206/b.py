n = int(input())

a = [i for i in range(1, 1000001)]
s = [0] * 1000001
for i in range(1000000):
    s[i + 1] = s[i] + a[i]

for i in range(1000000):
    if s[i] >= n:
        print(i)
        exit()
