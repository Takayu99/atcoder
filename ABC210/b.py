import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right


n = int(input())
s = list(input())

for i in range(n):
    if s[i] == "0":
        continue
    else:
        if i % 2 == 0:
            print("Takahashi")
        else:
            print("Aoki")
        break







