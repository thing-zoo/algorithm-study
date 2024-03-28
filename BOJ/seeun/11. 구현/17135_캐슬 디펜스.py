import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
n, m, d = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)] # 원본 배열
board = [castle[i][:] for i in range(n)] # 복사해서 사용할 배열

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(ox, oy): # bfs로 탐색하면서 [ox, oy]에서 공격할 적 위치 리턴
    candi = [] # 공격할 위치 후보들 저장
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append([ox, oy])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]: # 아직 방문하지 않은 곳
                    if board[nx][ny] == 1 and abs(ox - nx) + abs(oy - ny) <= d: # 적이 있고 거리가 d이하이면
                        candi.append([abs(ox - nx) + abs(oy - ny), nx, ny]) # 제거할 후보에 넣음
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    candi.sort(key = lambda x:(x[0], x[2])) # 거리, j 기준으로 오름차순
    if candi:
        return [candi[0][1], candi[0][2]] # 가장 가까운, 왼쪽에 있는 적 리턴
    else:
        return False


def countenemy(): # 남아있는 적 수 세기 + 한칸 내리기
    global board
    cnt = 0
    for i in range(n-2, -1, -1):
        cnt += board[i].count(1)
        board[i+1] = board[i][:]
    board[0] = [0] * m
    
    return cnt

board = [castle[i][:] for i in range(n)]
ans = 0 # 최대로 제거할 수 있는 적의 수 저장(정답 저장)

for loc in combinations(range(m), 3): # 적을 놓을 위치 구하기(조합)
    cnt = 0
    board = [castle[i][:] for i in range(n)] # 원본 배열 복사

    # 초기 적 수 구하기
    for i in range(n):
        cnt += board[i].count(1)

    tmpans = 0 # 이 조합에서 제거한 적 숫자
    while cnt > 0:
        attack = [] # 이번턴에 공격할 위치

        # 3명의 궁수 별 탐색
        for l in loc: 
            att = bfs(n, l) # 궁수 별로 공격할 적 위치 받아오기
            if att: # 공격할 적이 있으면
                attack.append(att) 
        
        # 공격할 적 제거
        for a in attack:
            if board[a[0]][a[1]] == 1:
                board[a[0]][a[1]] = 0 # 공격받은 적 제외
                tmpans += 1

        # 남은 적 수 카운트 & 적 아래로 이동
        cnt = countenemy() 
    ans = max(ans, tmpans)
print(ans)