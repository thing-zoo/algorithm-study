from collections import deque
def draw(d):
    if d == 0: # 동
        temp1 = dice[1]
        dice[1] = dice[4]
        temp2 = dice[3]
        dice[3] = temp1
        dice[4] = dice[6]
        dice[6] = temp2
    elif d == 1: # 남
        temp1 = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        temp2 = dice[5]
        dice[5] = temp1
        dice[6] = temp2
    elif d == 2: # 서
        temp1 = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        temp2 = dice[4]
        dice[4] = temp1
        dice[6] = temp2
    else: # 북
        temp1 = dice[1]
        dice[1] = dice[5]
        temp2 = dice[2]
        dice[2] = temp1
        dice[5] = dice[6]
        dice[6] = temp2

def bfs(x, y, b):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(dn):
            nx = x + dr[i]
            ny = y + dc[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 범위 밖이면
                continue
            if not visited[nx][ny] and board[nx][ny] == b:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
    return count

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dn = 4
dice = [i for i in range(7)]
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0 # 점수의 합
d = 0 # 초기 이동 방향은 동쪽
x, y = 0, 0 # 초기 주사위 위치

for _ in range(k): # k번 이동
    # 다음 좌표 결정
    nx = x + dr[d]
    ny = y + dc[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 밖이면
        d = (dn + d + 2)%dn # 방향 반대로
        nx = x + dr[d]
        ny = y + dc[d]
    x, y = nx, ny

    # 주사위 굴리기
    draw(d)

    a = dice[6] # 주사위 아랫면 정수
    b = board[nx][ny] # 도착칸 정수
    c = bfs(nx, ny, b) # 도착칸에서 연속으로 이동할 수 있는 칸의 수
    answer += b * c # 점수 획득

    # 다음 방향 결정
    if a > b:
        d = (d + 1)%dn # 시계 90도
    elif a < b:
        d = (dn + d - 1)%dn # 반시계 90도

print(answer)