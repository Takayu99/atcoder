import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right, insort, insort_left

q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
y = []
plus = 0
ans = []
for i in range(q):
    x = query[i]
    if x[0] == 1:
        y.append(x[1])
        flag = False
    elif x[0] == 2:
        plus += x[1]
    else:
        if not flag:
            y.sort(reverse=True)
        ans.append(y.pop() + plus)
        flag = True

for a in ans:
    print(a)