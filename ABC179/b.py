n = int(input())

judge = 0

for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        judge += 1
    else:
        judge = 0
    
    if judge >= 3:
        print("Yes")
        exit()

print("No")