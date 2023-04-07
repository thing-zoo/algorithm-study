import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ground = []

N, M, G, R = map(int, input().rstrip().split())


def bfs():
    cnt = 0
    color_ground = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    rq = deque()
    gq = deque()
    # 돌기전 배양액 뿌리기
    for i in R_list: # 빨간색 : 1
        x, y = queue[i]
        color_ground[x][y] = 1
        rq.append([x,y])
    for i in G_list: # 초록색 : 2
        x, y = queue[i]
        color_ground[x][y] = 2
        gq.append([x,y])
 
    red_cnt = -1
    while rq:
        red_cnt += 1
        tmplen = len(rq)
        for _ in range(tmplen): # 지금 큐에 있는 것 만큼만 퍼져나감
            x, y = rq.popleft()
            if color_ground[x][y] == 3: # 이미 꽃핀 자리이면 배양액 퍼져나갈 수 없음
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny< 0 or nx>=N or ny >= M:
                    continue
                if ground[nx][ny] == 0 or color_ground[nx][ny] == 3: #호수 or 이미 꽃 핀 곳
                    continue
                if color_ground[nx][ny] == 0 : # 아무것도 없으면 이동
                    color_ground[nx][ny] = 1 # 빨간 배양액 뿌리기
                    visited[nx][ny] = red_cnt + 1 # 언제 들어온 red인지 표시
                    rq.append([nx, ny])
          
        tmplen = len(gq)
        for _ in range(tmplen):
            x, y = gq.popleft()
            if color_ground[x][y] == 3:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny< 0 or nx>=N or ny >= M:
                    continue
                if ground[nx][ny] == 0 or color_ground[nx][ny] == 3: #호수 or 이미 꽃 핀 곳
                    continue
                if color_ground[nx][ny] == 0 or (color_ground[nx][ny] == 1 and visited[nx][ny] == red_cnt+1): # 아무것도 없거나 방금 빨간색 왔으면 이동
                    color_ground[nx][ny] += 2 
                    if color_ground[nx][ny] == 3: # 꽃 폈으면 cnt++
                        cnt += 1
                    else:gq.append([nx, ny]) # 꽃핀 자리는 담을 필요 없음
    return cnt


for _ in range(N):
    ground.append(list(map(int, input().rstrip().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if ground[i][j] == 2:
            queue.append([i, j]) # 뿌릴 수 있는 공간 저장

res = -1
for i in combinations(range(len(queue)), R+G): #뿌릴수 있는 공간 중에서 R+G개만 뽑아옴
    for j in combinations(range(R+G), R): # R+G개 중에 빨간색 뿌릴 공간 뽑아옴
        R_list = []
        G_list = []
        for k in range(R+G):
            if k in j: # 빨간색 뿌릴 공간이면
                R_list.append(i[k])
            else:
                G_list.append(i[k])
        res = max(res, bfs())
print(res)