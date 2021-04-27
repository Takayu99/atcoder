h, w, x, y = map(int, input().split())
s_list = []

for _ in range(h):
    s = list(input())
    s_list.append(s)

i = x - 1
j = y - 1
counter = 1

while(1):
    j += 1
    if j >= w:
        break
    if s_list[i][j] == ".":
        counter += 1
    elif s_list[i][j] == "#":
        break

j = y - 1

while(1):
    j -= 1
    if j < 0:
        break
    if s_list[i][j] == ".":
        counter += 1
    elif s_list[i][j] == "#":
        break

j = y - 1

while(1):
    i += 1
    if i >= h:
        break
    if s_list[i][j] == ".":
        counter += 1
    elif s_list[i][j] == "#":
        break

i = x - 1

while(1):
    i -= 1
    if i < 0:
        break
    if s_list[i][j] == ".":
        counter += 1
    elif s_list[i][j] == "#":
        break

print(counter)