def dfs(x, y, visited, count, total):
    global answer
    answer = max(answer, total) # answer 갱신
    if count == 4:# 최대 4쌍까지
        return
    for i in range(x, n):
        for j in range(n):
            if i == x and j < y:
                continue
            if visited[i][j]: # 이미 쌍이면 넘김
                continue
            visited[i][j] = True
            for d in range(4): # 인접한 나무 찾기
                ni = i + dx[d]
                nj = j + dy[d]
                if ni < 0 or nj < 0 or ni >= n or nj >= n: # 범위 외 넘김
                    continue
                if not visited[ni][nj]: # 아직 쌍이 아니면
                    visited[ni][nj] = True
                    dfs(i, j, visited, count+1, total+board[i][j]+board[ni][nj])
                    visited[ni][nj] = False
            visited[i][j] = False
                
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
answer = 0

dfs(0,0,visited,0,0)
print(answer)