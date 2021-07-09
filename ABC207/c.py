n = int(input())
tlr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n - 1):
    ti, li, ri = tlr[i][0], tlr[i][1], tlr[i][2]
    li *= 10
    ri *= 10
    if ti == 2:
        ri -= 1
    elif ti == 3:
        li += 1
    elif ti == 4:
        ri -= 1
        li += 1
    for j in range(i + 1, n):
        tj, lj, rj = tlr[j][0], tlr[j][1], tlr[j][2]
        lj *= 10
        rj *= 10
        if tj == 2:
            rj -= 1
        elif tj == 3:
            lj += 1
        elif tj == 4:
            rj -= 1
            lj += 1
        
        if not((li < lj and ri < lj) or (li > rj and ri > rj)):
            ans += 1
        # if max(li, lj) <= min(ri, rj):
        #     ans += 1
print(ans)