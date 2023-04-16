import copy
def dfs(start, visited):
    global answer
    if start == len(cctvs): # 모든 cctv의 한 방향에 대한 감시영역을 확인했다면
        count = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0: # 사각지대 세기
                    count += 1
        answer = min(answer, count) # 사각지대의 최솟값
        return

    for i in range(start, len(cctvs)):
        cctv, (x, y) = cctvs[i]
        for dir in dirs[cctv-1]: # 해당 cctv의 방향의 경우의 수
            copy_visited = copy.deepcopy(visited)
            for dx, dy in dir: # 방향 마다
                nx, ny = x, y
                while True: # 감시 영역 확인하기
                    nx, ny = nx+dx, ny+dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if 0 <= graph[nx][ny] < 6: # 감시 가능하고
                        if graph[nx][ny] == 0: # 빈칸이면
                            visited[nx][ny] = 1
                    if graph[nx][ny] == 6: # 벽을 만나면
                        break # 종료
            dfs(i+1, visited) # 다음 cctv로
            visited = copy_visited

dir1 = [[(1,0)],[[0,1]],[[-1,0]],[[0,-1]]]
dir2 = [[(1,0),(-1,0)], [(0,1),(0,-1)]]
dir3 = [[(1,0),(0,1)], [(1,0),(0,-1)], [(-1,0),(0,-1)], [(-1,0),(0,1)]]
dir4 = [[(-1,0),(0,1),(1,0)], [(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)], [(0,-1),(-1,0),(0,1)]]
dir5 = [[(1,0),(0,1),(-1,0),(0,-1)]]
dirs = [dir1, dir2, dir3, dir4, dir5]
n, m = map(int, input().split())
graph = []
cctvs = []
visited = [[0]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 0 < graph[i][j] < 6: # cctv면
            cctvs.append((graph[i][j], (i,j))) # 번호, 좌표
            visited[i][j] = -1
        elif graph[i][j] == 6: # 벽이면
            visited[i][j] = -1
answer = n*m
dfs(0, visited)
print(answer)