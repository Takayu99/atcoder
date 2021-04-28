n = int(input())
a = list(map(int, input().split()))

ans = 2**30

for mask in range(1 << (n - 1)): #for mask in range(2 ** (n - 1))
    val_xor = 0
    tmp = a[0]

    for i in range(1, n): 
        if mask & 1 << (i - 1): # if mask & 2**(i - 1)
            val_xor = val_xor ^ tmp
            tmp = 0
        tmp |= a[i]
    
    val_xor ^= tmp
    ans = min(ans, val_xor)

print(ans)


"""
ビット演算
排他的論理和(XOR)：複数個の場合，1の個数が奇数なら1，偶数なら0

"""