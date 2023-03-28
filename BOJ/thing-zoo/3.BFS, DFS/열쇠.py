from collections import deque
def bfs():
    answer = 0
    q = deque()
    q.append([0,0])
    visited = [[False]*(w+2) for _ in range(h+2)]
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h + 2 and 0 <= nx < w + 2 and not visited[ny][nx]:
                if graph[ny][nx] != "*":
                    if graph[ny][nx] == "$": # 문서면
                        answer += 1          # 카운트
                        graph[ny][nx] = "."
                        visited[ny][nx] = True
                        q.append([ny,nx])
                    if graph[ny][nx] == ".":
                        visited[ny][nx] = True
                        q.append([ny,nx])
                    elif graph[ny][nx].islower(): # 열쇠면
                        key.append(graph[ny][nx]) # 집어 넣고
                        graph[ny][nx] = "."       # 빈공간으로
                        visited = [[False]*(w+2) for _ in range(h+2)] # 방문표시 초기화
                        q.clear()
                        visited[ny][nx] = True
                        q.append([ny, nx])
                        break
                    else: # 문이면
                        a = graph[ny][nx].lower()
                        if a in key: # 열쇠가 있으면
                            graph[ny][nx] = "."       # 빈공간으로
                            q.append([ny,nx])
                        visited[ny][nx] = True
    return answer

dx = [1,0,-1,0]; dy = [0,1,0,-1]
t = int(input())
for _ in range(t):
    h,w = map(int, input().split())
    graph = [["."]*(w+2) for _ in range(h+2)]
    key = []
    for i in range(h):
        tmp = list(input())
        for j in range(w):
            graph[i+1][j+1] = tmp[j]
    key = list(input())
    print(bfs())