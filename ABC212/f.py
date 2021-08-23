import math
from collections import deque, Counter
from itertools import product, combinations, permutations
from bisect import bisect, bisect_left, bisect_right


cnt = Counter()
a = [2, 4, 1, 8, 3, 10, 7, 1, 2, 2]
cnt = Counter(a)
print(max(cnt))