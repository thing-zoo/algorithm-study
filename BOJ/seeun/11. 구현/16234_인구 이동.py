from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global visited, union, nationality
    queue = deque()
    visited[x][y] = True

    queue.append([x, y])
    union.append([x, y])
    nationality += nations[x][y]
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print("four", nx, ny, visited)
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if L<= abs(nations[x][y]-nations[nx][ny]) <= R:
                    union.append([nx, ny])
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    nationality += nations[nx][ny]
                

n, L, R = map(int, input().split())
nations = []
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    nations.append(list(map(int, input().split())))


cnt = 0
flag = True
while flag: # n차 인구이동
    flag = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False: # 도시 돌면서 연합지역
                union = []
                nationality = 0
                bfs(i, j) # 연합지역 만들기
                if len(union) == 1: # 연합국가에 본인 밖에 없으면 연합 진행 안됨
                    continue
                flag = True # 연합 하나라도 맺었으면 True로 변경

                # 연합국가 인구수 조정
                for u in union:
                    nations[u[0]][u[1]] = nationality//len(union)
  
    if not flag: # 모든 국가가 연합을 맺지 못했으면
        break
    cnt += 1

print(cnt)