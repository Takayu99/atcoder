import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right
import heapq

H, W, N = map(int, input().split())
h = []
w = []
for i in range(N):
    a, b = map(int, input().split())
    h.append(a)
    w.append(b)


sorth = sorted(list(set(h)))
sortw = sorted(list(set(w)))
for i in range(N):
    print(bisect(sorth, h[i]), bisect(sortw, w[i]))



