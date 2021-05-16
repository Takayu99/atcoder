n, m = map(int, input().split())

frd = [list(map(int, input().split())) for _ in range(m)]

dp = [0] * (n + 1)

for a, b in frd:
    dp[a] = dp[a] | (1 << b) | dp[b]
    dp[b] = dp[b] | (1 << a) | dp[a]

def bit_count(n):
    #2進数表記した時の1の個数を返す
    x = 0
    while(n > 0):
        if n & 1:
            x += 1
        n = n >> 1
    return x



ans = 0
for x in dp:
    ans = max(ans, bit_count(x))

print(ans)


