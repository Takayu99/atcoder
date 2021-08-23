import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right, insort, insort_left
import heapq

q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
a = []
heapq.heapify(a)
plus = 0
ans = []
for i in range(q):
    if query[i][0] == 1:
        heapq.heappush(a, query[i][1] - plus)
    
    elif query[i][0] == 2:
        plus += query[i][1]
    
    else:
        ans.append(heapq.heappop(a) + plus)

for x in ans:
    print(x)
