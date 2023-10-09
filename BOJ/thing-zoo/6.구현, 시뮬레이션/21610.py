from collections import deque
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] # 물의양
cloud = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]) # 구름의 초기좌표

for _ in range(m):
    d, s = map(int, input().split()) # 방향, 거리
    visited = [[False]*n for _ in range(n)] # 시간초과때문에 추가

    for _ in range(len(cloud)):
        a, b = cloud.popleft()
        # 구름 이동시키기
        na = (n + a + di[d-1]*s)%n
        nb = (n + b + dj[d-1]*s)%n

        # 비 내리기
        board[na][nb] += 1

        cloud.append((na, nb))
        visited[na][nb] = True # 구름 좌표 표시

    # 물복사버그 시전
    # 어차피 구름구역은 최소 1이상이므로 변화된 값은 고려안해도됨
    while cloud:
        a, b = cloud.popleft()
        count = 0 # 대각선 물 여부 개수
        for j in range(8): # 홀수가 대각선
            if j%2 == 0: continue

            na = a + di[j]
            nb = b + dj[j]
            if na < 0 or na >= n or nb < 0 or nb >= n:
                continue
            if board[na][nb] > 0: 
                count += 1
        board[a][b] += count

    # 구름 생성
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] >= 2:
                cloud.append((i, j))
                board[i][j] -= 2

# 총 물의 양 계산
answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]
print(answer)