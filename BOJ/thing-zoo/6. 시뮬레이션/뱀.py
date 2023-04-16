n = int(input())
board = [[0]*n for _ in range(n)]
order = []
APPLE = 1
SNAKE = 2

# 배열 초기화
board[0][0] = SNAKE # 시작점에 뱀 위치
for _ in range(int(input())): # 사과 위치 입력받기
    i, j = map(int, input().split())
    board[i-1][j-1] = APPLE
for _ in range(int(input())):
    t, c = input().split() # t, c: 초, 방향
    order.append([int(t), c])

# 시작
time = 0    # 현재 시간
x, y = 0, 0 # (0,0)에서 시작
dir = 0     # 처음엔 오른쪽을 향하고 있음
snake = [[0,0]] # 현재 뱀이 있는 모든 위치
dx = [0,1,0,-1]; dy = [1,0,-1,0] # 우하좌상
shift = [[3, 1], [0, 2], [1, 3], [2, 0]] # 우하좌상에 따른 좌우 방향 전환 정보
while True:
    time += 1
    # 현방향으로 이동
    x, y = x + dx[dir], y + dy[dir]
    # 벽이나 자기자신과 부딪히면 종료
    if (x < 0 or x >= n or y < 0 or y >= n) or (board[x][y] == SNAKE):
        print(time)
        break
    if board[x][y] != APPLE: # 사과가 없다면
        i,j = snake.pop(0)   # 꼬리 줄이기
        board[i][j] = 0
    board[x][y] = SNAKE # 뱀 표시
    snake.append([x,y])
    if order:
        t, c = order[0]
        if time == t: # 현재초에 대한 방향 전환 정보가 있다면
            if c == "L": c = 0
            else: c = 1
            dir = shift[dir][c] # 방향 전환
            order.pop(0)