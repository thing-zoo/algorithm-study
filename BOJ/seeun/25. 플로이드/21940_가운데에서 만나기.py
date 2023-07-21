import sys
input = sys.stdin.readline
n, m = map(int , input().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

friend_num = int(input())
friend = list(map(int, input().split()))

for i in range(n+1):
    graph[i][i] = 0

# 플로이드로 편도 최소 거리 다 구해놓기
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

mindist = float('inf')
ans = []
for i in range(1, n+1): # 목적지가 i일 때 왕복 거리 구하기
    tmp = 0
    for j in range(friend_num):
        f = friend[j] # j번째 친구의 위치 f
        tmp = max(graph[f][i] + graph[i][f], tmp) # 목적지가 i일때 왕복 거리가 가장 큰 친구의 거리 저장

    if mindist > tmp: # 왕복거리 최대값이 최소가 되는 지점 구하기
        mindist = tmp
        ans = [i]
    elif mindist == tmp: # 최소값과 같으면 정답 리스트에 지점 추가
        ans.append(i)

print(*sorted(ans))