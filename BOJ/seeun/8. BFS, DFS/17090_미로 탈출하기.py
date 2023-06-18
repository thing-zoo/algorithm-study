import sys
sys.setrecursionlimit(30000000)
n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]

# 그 자리에서 나갈 수 있으면 True로 변경
possible = [[-1]*m for _ in range(n)]

def dfs(x, y):
    global possible
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    if possible[x][y] != -1: # 이미 검사한 곳이라면 그 자리의 결과값 리턴
        return possible[x][y]
    elif visited[x][y] == True: # 무한 굴레에 빠지는 루트라면 False
        return False
    elif possible[x][y] == -1: # 아직 검사 안한곳이면 검사하러 가기
        visited[x][y] = True # 방문처리
        if maze[x][y] == "U":
            possible[x][y] = dfs(x-1, y)
        elif maze[x][y] == "R":
            possible[x][y] = dfs(x, y+1)
        elif maze[x][y] == "L":
            possible[x][y] = dfs(x, y-1)
        elif maze[x][y] == "D":
            possible[x][y] = dfs(x+1, y)
        return possible[x][y]
        
cnt = 0
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if possible[i][j] == -1: # 아직 검사 안한 곳이면
            possible[i][j] = dfs(i, j)

        if possible[i][j]: # 그 자리가 True라면 탈출할 수 있는 자리
            cnt += 1
print(cnt)