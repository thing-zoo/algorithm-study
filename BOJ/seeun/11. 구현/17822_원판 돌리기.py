from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def delete(x, y):
    global visited, cnt
    queue = deque()
    queue.append([x, y, circles[x][y]])
    res = False
    
    while queue:
        x, y, num= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0:
                ny = m-1
            elif ny == m:
                ny = 0
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if num > 0 and circles[nx][ny] == num:#인접한 위치가 같은 숫자이면
                    visited[nx][ny] = True
                    visited[x][y] = True
                    circles[nx][ny] = 0 # 숫자 삭제
                    circles[x][y] = 0
                    queue.append([nx, ny, num])
                    res = True
                    cnt += 1
    return res

# Main ==================================================================================
n, m, turn = map(int, input().split())
circles = []
for _ in range(n):
    circles.append(deque(list(map(int, input().split()))))


for _ in range(turn):
    visited = [deque([False]*m) for _ in range(n)]
    x, d, k = map(int, input().split())

    # 원판 돌리기 ==============================
    if d == 0: # 시계
        t = 1
        while x*t-1<n:
            circles[x*t-1].rotate(k)
            t += 1
    elif d == 1: # 반시계
        t = 1
        while x*t-1<n:
            circles[x*t-1].rotate(-k)
            t += 1

    # 인접한 숫자들 지우기==========================
    visited = [deque([False]*m) for _ in range(n)]
    flag = False
    cnt = 0
    num_sum = 0
    num_cnt = 0
    for i in range(n):
        for j in range(m):
            if circles[i][j] > 0: # 숫자가 있으면
                num_sum += circles[i][j] # 카운트, 숫자 세기
                num_cnt += 1
                if not visited[i][j]: # 아직 방문 안했으면
                    tmp = delete(i, j)

    # 삭제할 숫자가 없었다면 +1 -1 ====================
    if cnt == 0 and num_cnt>0:
        avg = num_sum/num_cnt
        for r in range(n):
            for c in range(m):
                if circles[r][c] != 0 and circles[r][c] > avg:
                    circles[r][c] -=1
                elif circles[r][c] != 0 and circles[r][c] < avg:
                    circles[r][c] += 1

circle_sum = 0
for i in range(n):
    circle_sum += sum(circles[i])
print(circle_sum)