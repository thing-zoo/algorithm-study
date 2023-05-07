import math, sys
input = sys.stdin.readline
n = int(input())
d = [0] * (n+1)
d[1] = 1
# 1, 4, 9, 16
idx = 1
for i in range(2, n+1):
        d[i] = d[1]+d[i-1] # 초기값 
        for j in range(2, int(math.sqrt(i))+1):
            d[i] = min(1+d[i-j*j], d[i])

print(d[n])