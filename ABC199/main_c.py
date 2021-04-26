n = int(input())
s = input()
q = int(input())
src = []



for i in range(q):
    src.append(list(map(int, input().split())))

for i in range(q):
    if src[i][0] == 1:
        a = src[i][1] - 1
        b = src[i][2] - 1
        s = s[0:a] + s[b] + s[a + 1:b] + s[a] + s[b + 1:2 * n]

    elif src[i][0] == 2:
        # s[0:n], s[n+1:2 * n] = s[n+1:2 * n], s[0:n]
        front = s[0:n]
        back = s[n : n*2]
        s = back + front

print(s)

