from collections import deque
def play():
    is_moved = True
    while is_moved:
        is_moved = False
        for p in range(1, P+1): # 플레이어 순서대로 턴이 돌아감
            if not castle[p]: # 이동할게 없으므로
                continue
            q = castle[p]
            for _ in range(S[p]): # 이동가능한 만큼 반복
                if not q: # 이동할 게 없으므로
                    break
                for _ in range(len(q)): # 각 위치 한 번 이동
                    y, x = q.popleft()
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == '.': #유효범위이고 빈칸이면
                            graph[ny][nx] = str(p) # 방문 표시
                            q.append([ny, nx])
                            result[p] += 1 # 성의 수 증가
                            is_moved = True

dx = [1,0,-1,0]; dy = [0,1,0,-1]
graph = []
N, M, P = map(int, input().split())
S = [0]+list(map(int, input().split()))
castle = [ deque() for _ in range(P+1) ]
result = [0]*(P+1)
for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] != '.' and graph[i][j] != '#':
            p = int(graph[i][j])
            result[p] += 1
            castle[p].append([i, j])
play()
print(*result[1:])