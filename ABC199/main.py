import numpy as np

e = 200
v = 0.3

q11 = e/(1 - v**2)
q12 = v * e / (1 - v**2)
q66 = e/(2 * (1 + v))

Q = np.array([[q11, q12, 0], [q12, q11, 0], [0, 0, q66]])

s = np.array([1, 0.5, 0.3])

dst = np.dot(Q, s)

print(dst)