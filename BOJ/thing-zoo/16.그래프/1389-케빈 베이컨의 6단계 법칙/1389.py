n, m = map(int, input().split())
dist = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    dist[i][j] = dist[j][i] = 1

# 플로이드 워셜 알고리즘: 모든정점간 최단거리
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: continue # 자기자신은 건너뛰기
            if dist[i][k] and dist[k][j]: # 둘다 값이 있으면
                if dist[i][j] == 0: # i-j로 길이 없었던 경우
                    dist[i][j] = dist[i][k] + dist[k][j] # 갱신
                else:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) # 갱신
            

min_value = 1e9
answer = 0
for i in range(1, n+1):
    temp = sum(dist[i])
    if min_value > temp:
        min_value = temp
        answer = i
print(answer)