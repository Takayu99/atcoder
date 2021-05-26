a = [0.25, 0.11, 0.65, 0.47, 0.26]
b = []
for x in a:
    b.append(x / sum(a))
c = b
for i in range(1, 5):
    c[i] = c[i] + c[i - 1]
print(c)