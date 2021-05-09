from collections import Counter
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = int(input())

a = list(map(int, input().split()))
b = [x % 200 for x in a]
counter = dict(Counter(b))
value = counter.values()

ans = 0

for v in value:
    if v >= 2:
        ans += combinations_count(v, 2)

print(ans)