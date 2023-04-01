def z(n, r, c):
    if n == 0: return 0
    half = 1 << (n-1) # 2^(n-1)
    if r < half and c < half: return z(n-1, r, c)                               #1번블럭
    elif r < half and c >= half: return half*half + z(n-1, r, c-half)           #2번블럭
    elif r >= half and c < half: return 2*half*half + z(n-1, r-half, c)         #3번블럭
    elif r >= half and c >= half: return 3*half*half + z(n-1, r-half, c-half)   #4번블럭

n, r, c = map(int, input().split())
print(z(n, r, c))