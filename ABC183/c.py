#Travel

import itertools

N, K = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(N)]

l = [i + 1 for i in range(N - 1)]

cnt = 0
for v in itertools.permutations(l):
    tmp = t[0][v[0]]
    for i in range(1, N - 1):
        tmp += t[v[i]][v[i - 1]]
    tmp += t[v[-1]][0]
    if tmp == K:
        cnt += 1 

print(cnt)