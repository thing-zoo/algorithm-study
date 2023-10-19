# 토네이도 방향: 좌 하 우 상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

# 토네이도 비율 배열
tornado = [[0,0,0.02,0,0],
           [0,0.1,0.07,0.01,0],
           [0.05,-3,-2,-1,0],
           [0,0.1,0.07,0.01,0],
           [0,0,0.02,0,0]]
m = 5

# 토네이도는 1 1 2 2 3 3 , ... 칸마다 회전한다
repeat = 1
count = 0
d = 0

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = 0 # 격자 밖으로 나간 모래의 양

def rotate():
    rotated = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated[m-j-1][i] = tornado[i][j]
    return rotated

x = y = n//2 # 가운데에서 시작
while True:
    for _ in range(repeat): # repeat칸 이동
        ny = y + dy[d]
        nx = x + dx[d]
        total = 0
        for i in range(m):
            for j in range(m):
                if tornado[i][j] <= 0: continue
                if i+ny-2 < 0 or i+ny-2 >= n or j+nx-2 < 0 or j+nx-2 >= n: # 격자 밖이면
                    result += int(tornado[i][j]*board[ny][nx]) # 결과에 더하기
                else: # 격자 내면
                    board[i+ny-2][j+nx-2] += int(tornado[i][j]*board[ny][nx]) # 격자에 더하기
                total += int(tornado[i][j]*board[ny][nx]) # 비율 모래 저장해두기

        # a의 위치
        ny2 = y + 2*dy[d]
        nx2 = x + 2*dx[d]
        if ny2 < 0 or ny2 >= n or nx2 < 0 or nx2 >= n: # 격자 밖이면
            result += board[ny][nx] - total # 결과에 더하기
        else: # 격자 내면
            board[ny2][nx2] += board[ny][nx] - total # 격자에 더하기

        board[ny][nx] = 0 # 모래비우기
        
        # 이동
        y = ny
        x = nx
        
        if y == x == 0:  # 종료
            print(result)
            exit(0)

    # 현재 방향에 대해 repeat만큼 반복
    d = (d+1)%4
    tornado = rotate() # 회전
    count += 1 # count 증가
    if count == 2: # 2번 반복했다면
        count = 0   # count 초기화
        repeat += 1 # repeat 증가