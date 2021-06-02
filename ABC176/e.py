H, W, m = map(int, input().split())

b = []
col = [0] * (W + 1)
row = [0] * (H + 1)
for _ in range(m):
    h, w = map(int, input().split())
    # h -= 1
    # w -= 1
    col[w] += 1
    row[h] += 1
    b.append([h, w])

rmax = max(row)
cmax = max(col)
r = []
c = []
for i in range(W + 1):
    if col[i] == cmax:
        c.append(i)
for i in range(H + 1):
    if row[i] == rmax:
        r.append(i)
    
for h in r:
    for w in c:
        if not [h, w] in b:
            print(rmax + cmax)
            exit()

print(rmax + cmax - 1)



# col.sort(reverse=True)
# row.sort(reverse=True)

# if col[0][1] == row[0][1]:
#     ans = max(col[0][0] + row[1][0], col[1][0] + row[0][0])
# else:
#     ans = col[0][0] + row[0][0]

# def solve(i, j):
#     if [row[j][1], col[i][1]] in b:
#         return max(solve(i + 1, j), solve(i, j + 1), col[i][0] + row[j][0] - 1)
#     else:
#         return col[i][0] + row[j][0]

# ans = solve(0, 0)

# print(ans)
# print(col)
# print(row)
