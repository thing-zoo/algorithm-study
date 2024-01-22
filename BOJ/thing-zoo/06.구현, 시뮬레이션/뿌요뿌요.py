from collections import deque
def bfs(start, visited):
    dx = [1,0,-1,0]; dy = [0,1,0,-1]
    q = deque()
    q.append(start)
    color = board[start[0]][start[1]]
    puyo = [start] # 뿌요그룹을 담을 배열
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    puyo.append([nx, ny])
    return puyo

def bomb(puyo):
    for i, j in puyo:
        board[i][j] = "."

def gravity(): # 밑에서부터 뿌요 내리기
    for j in range(m-1, -1, -1): 
        for i in range(n-1, -1, -1): # 모든 좌표 중에
            if board[i][j] != '.': # 뿌요라면
                for k in range(n-1, i, -1): # 뿌요 밑 공간 중에
                    if board[k][j] == '.': # 밑에 내려갈 공간이 있다면
                        board[k][j] = board[i][j] # 그 공간에 뿌요를 내리고
                        board[i][j] = '.' # 뿌요자리는 빈칸으로
                        break

def play():
    combo = 0
    while True:
        flag = False
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and board[i][j] != '.': # 방문 안한 색깔이면
                    visited[i][j] = 1 # 방문표시
                    puyo = bfs([i,j], visited) # 뿌요 영역 구하기
                    if len(puyo) >= 4:
                        flag = True # 아직 터뜨릴게 있음
                        bomb(puyo) # 터뜨리기
        if not flag: # 터뜨릴게 없으면
            break # 종료
        gravity()  # 중력작용 
        combo += 1 # 연쇄 카운트
    return combo

n = 12; m = 6
board = [ list(input()) for _ in range(n) ]
print(play())