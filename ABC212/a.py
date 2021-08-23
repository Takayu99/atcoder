import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right


a, b = map(int, input().split())
if a == 0:
    print("Silver")
elif b == 0:
    print("Gold")
else:
    print("Alloy")
