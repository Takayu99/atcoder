

Est = 200
vst = 0.33
Eal = 70
val = 0.35

z = [-8, -5 ,3, 8]

q11st = Est / (1 - vst * vst)
q12st = vst * Est / (1 - vst * vst)
q11al = Eal / (1 - val * val)
q12al = val * Eal / (1 - val * val)

b11 = (q11st * (z[1]**2 - z[0]**2) + q11al * (z[2]**2 - z[1] ** 2) + q11st * (z[3] ** 2 - z[2] ** 2)) / 2
b12 = (q12st * (z[1]**2 - z[0]**2) + q12al * (z[2]**2 - z[1] ** 2) + q12st * (z[3] ** 2 - z[2] ** 2)) / 2

print(b11)
print(b12)