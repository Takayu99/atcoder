import math
from collections import deque, Counter
from itertools import product, combinations, permutations

a, b = map(int, input().split())
if b - a + 1 <= 0:
    print(0)
else:
    print(b - a  + 1)