
Est = 200
vst = 0.33
Eal = 70
val = 0.35

z = [-8, -5 ,5, 8]

q11st = Est / (1 - vst * vst)
q12st = vst * Est / (1 - vst * vst)
q11al = Eal / (1 - val * val)
q12al = val * Eal / (1 - val * val)

d11 = (q11st * (z[1] ** 3 - z[0] ** 3)+ q11al * (z[2] ** 3 - z[1] ** 3)+ q11st * (z[3] ** 3 - z[2] ** 3)) / 3
d12 = (q12st * (z[1] ** 3 - z[0] ** 3)+ q12al * (z[2] ** 3 - z[1] ** 3)+ q12st * (z[3] ** 3 - z[2] ** 3)) / 3


print(d11)
print(d12)


