from itertools import combinations
n, k = map(int ,input().split())
d = [[0] * (n+1) for _ in range(n+1)]

d[1][0] = 1
d[1][1] = 1

for i in range(2, n+1):
    d[i][0] = 1
    d[i][i] = 1
    for j in range(1, i+1):
        d[i][j] = (d[i-1][j] + d[i-1][j-1]) % 10007
    
print(d[n][k]%10007)