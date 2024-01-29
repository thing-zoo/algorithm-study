def dfs(board, i, count):
    global max_black, max_white
    if i == len(board): # 모든 좌표를 방문했다면
        x, y = board[-1]
        if chess[x][y]: max_black = max(max_black, count)
        else: max_white = max(max_white, count)
        return  # 종료

    x, y = board[i] # 현재칸이
    if not diagonal1[x+y] and not diagonal2[x-y+n-1]: # 놓을수있다면
        diagonal1[x+y] = True # 놓기
        diagonal2[x-y+n-1] = True
        dfs(board, i+1, count+1) # 다음칸으로
        diagonal1[x+y] = False #놓지 않기
        diagonal2[x-y+n-1] = False
        dfs(board, i+1, count) # 다음칸으로
    else: # 놓을 수 없다면
        dfs(board, i+1, count) # 다음칸으로

n = int(input())
data = []
chess = [ [0]*n for _ in range(n)] # 검은칸: 1, 흰칸: 0
black = [] # 놓을 수 있는 검은칸
white = [] # 놓을 수 있는 흰칸
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        chess[i][j] = (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)
        if data[i][j] and chess[i][j]:
            black.append((i,j))
        elif data[i][j] and not chess[i][j]:
            white.append((i,j))
diagonal1 = [False]*(2*n-1) # x+y
diagonal2 = [False]*(2*n-1) # x-y+n-1
max_black = 0
max_white = 0
if black: dfs(black, 0, 0)
if white: dfs(white, 0, 0)
print(max_black+max_white)