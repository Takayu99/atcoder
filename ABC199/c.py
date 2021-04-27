# n = int(input())
# s = list(input())
# q = int(input())
# for i in range(q): #計算量O(Q)
#     t, a, b = map(int, input().split())
#     if t == 1:
#         a -= 1
#         b -= 1
#         s[a], s[b] = s[b], s[a]
    
#     elif t == 2:
#         front = s[0 : n] #計算量O(N)
#         back = s[n : n*2]
#         s = back + front

# s = "".join(s)

# print(s)
#O(Q*N)

"""
計算量のオーダーはO(Q*N)
T=2のときに計算量が多くなってしまう
"""

#改良版
n = int(input())
s = list(input())
q = int(input())

flag = False

for _ in range(q): #計算量O(Q)
    t, a, b = map(int, input().split())
    
    if t  == 1:
        a -= 1
        b -= 1
        if flag:
            if a >= n:
                a -= n
            else:
                a += n
            
            if b >= n:
                b -= n
            else:
                b += n
        
        s[a], s[b] = s[b], s[a]

    else:
        flag = not flag
    
if flag:
    s = s[n:] + s[:n] #計算量O(N)
    
s = "".join(s)

print(s)

#O(Q+N)