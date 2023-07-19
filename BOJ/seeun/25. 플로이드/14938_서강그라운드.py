import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
items = [0]
items.extend(list(map(int, input().split())))
ground = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    ground[a][b] = c
    ground[b][a] = c
for i in range(n+1):
    ground[i][i] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            ground[i][j] = min(ground[i][j], ground[i][k] + ground[k][j])


ans = 0
for i in range(1, n+1): # 떨어지는 지점이 i일 때
    tmp = 0 # 시작점이 i일 때 얻을 수 있는 아이템 개수 저장
    for j in range(1, n+1):
        if ground[i][j] <= m:
            tmp += items[j]
    ans = max(ans, tmp) # 모든 시작점 중에 가장 많이 얻을 수 있는 아이템 개수 저장
print(ans)