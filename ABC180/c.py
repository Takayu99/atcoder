import math

n = int(input())
r = math.ceil(math.sqrt(n))
ans = set()

for i in range(1, r + 1):
    if n % i == 0:
        ans.add(i)
        ans.add(n // i)
        
        
for a in sorted(ans):
    print(a)



