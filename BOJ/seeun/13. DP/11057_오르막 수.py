n = int(input())

d = [[0]*10 for _ in range(n+1)]

for i in range(10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10): #j로 시작하는 수
        for k in range(j, 10): #길이가 i-1인, j보다 크거나 같은수는 모두 올수 있음
            d[i][j] += d[i-1][k]
print(sum(d[n])%10007)