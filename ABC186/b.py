# h, w = map(int, input().split())

# a = [list(map(int, input().split())) for i in range(h)]
# min_list = []

# for i in a:
#     min_list.append(min(i))
# d = min(min_list)

# ans = 0
# for i in a:
#     for j in i:
#         ans += j - d

# print(ans)

import numpy as np

h, w = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(h)]
A = np.array(A)
print(np.sum(A - np.min(A)))