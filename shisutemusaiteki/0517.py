import numpy as np
import math
from math import sin, cos

theta = math.radians(30)
u1 = 76.374
u2 = 85.73
u3 = 19.71
u4 = 22.61
u5 = 26.88

q11 = u1 + u2 * cos(2 * theta) + u3 * cos(4 * theta)
q12 = u4 - u3 * cos(4 * theta)

print(q11)
print(q12)

