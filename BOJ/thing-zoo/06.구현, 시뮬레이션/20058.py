from collections import deque
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
n, q = map(int, input().split())
board = [list(map(int, input().split())) for i in range(2**n)]
level = list(map(int, input().split()))

def bfs(x, y): # 얼음 덩어리 칸 수 구하기
    q = deque([(x,y)])
    visited[x][y] = True
    count = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= 2 ** n or nj < 0 or nj >= 2 ** n:
                continue
            if board[ni][nj] > 0 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
                count += 1
    return count

def rotate(i, j, size): # 시계방향으로 90도 회전시키기
    rotated = [[0]*size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            rotated[y][size-x-1] = board[i+x][j+y]
    return rotated

def firestorm(size):
    # 회전시키기
    if size > 1:
        for i in range(0, 2**n, size):
            for j in range(0, 2**n, size):
                rotated = rotate(i, j, size)
                for x in range(size):
                    for y in range(size):
                        board[i+x][j+y] = rotated[x][y]
    # 얼음 양 줄이기
    candi = []
    for i in range(2**n):
        for j in range(2**n):
            if board[i][j] == 0: continue
            count = 0 # 인접한 얼음있는 칸 개수
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 0 or ni >= 2**n or nj < 0 or nj >= 2**n:
                    continue
                if board[ni][nj] > 0: count += 1
            if count < 3:
                candi.append((i, j))
    for i, j in candi:
        board[i][j] -= 1

for l in level:
    firestorm(2**l)

total_ice = 0 # 총 얼음의 양
max_count = 0 # 가장 큰 얼음 덩어리 칸 수
visited = [[False]*(2**n) for _ in range(2**n)]
for i in range(2 ** n):
    for j in range(2 ** n):
        total_ice += board[i][j]
        if not visited[i][j] and board[i][j] != 0:
            max_count = max(max_count, bfs(i, j))

print(total_ice)
print(max_count)
