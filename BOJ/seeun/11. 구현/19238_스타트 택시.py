from collections import deque
N, M, energy = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] # 지도 정보
passenger = [[0] * N for _ in range(N)] # 손님의 위치 저장
tmp = list(map(int, input().split())) # 택시 위치 입력
tx, ty = tmp[0]-1, tmp[1]-1 # 택시 위치

passenger_list = [[]] # 손님 정보 저장할 리스트
for _ in range(M):
    a, b, c, d = map(int, input().split())
    a, b, c, d = a-1, b-1, c-1, d-1
    passenger_list.append([a, b, c, d])
complete = [False] * (M+1)

for i in range(1, M+1):
    # i의 출발지는 i, 목적지는 -i로 표시
    p = passenger_list[i]
    passenger[p[0]][p[1]] = i
    i += 1

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 승객을 목적지로 태우기
def work(sx, sy):
    num = passenger[sx][sy]
    gx, gy = passenger_list[num][2], passenger_list[num][3] # 목적지 좌표
    global energy, tx, ty
    queue = deque()
    visited = [[False]*N for _ in range(N)]
    queue.append([tx, ty, 0]) # x, y, 거기까지 가는데 들었던 연료 양
    visited[tx][ty] = True
    find = False
    while queue:
        x, y, oil = queue.popleft()
        if x == gx and y == gy and energy - oil > -1: # 해당 손님의 목적지에 도착했고, 갔을 때 기름 양이 0 이상이면
            energy -= oil # 지금까지 쓴 연료 빼기
            energy += oil*2 # 쓴 연료의 두배 충전
            find = True
            tx, ty = x, y # 택시 기사 위치 갱신
            complete[num] = True
            # print(passenger[sx][sy], '손님 목적지에 도착함', x, y, '사용한 에너지', oil, '남은 전체 에너지', energy)
            return True # 위치 리턴
        
        if energy - oil < 0: # 위치 못찾았는데 연료 바닥나면 끝남
            continue

        for i in range(4): # 위 좌 우 하
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not board[nx][ny]: # 범위 내 & 아직 방문 안함 & 벽 아님
                visited[nx][ny] = True
                queue.append([nx, ny, oil + 1])

    if not find: # 큐 다 돌았는데 아직 못도착했으면
        # print(passenger[sx][sy], '손님 목적지에 도착 못함!!!!')
        return False


# 가장 가까운 승객 찾기 - 승객 찾으면 후보 리스트에 넣어줌
def find_passenger():
    global energy, candi
    queue = deque()
    visited = [[False]*N for _ in range(N)]

    queue.append([tx, ty, 0])
    visited[tx][ty] = True

    while queue:
        x, y, oil = queue.popleft()
        if passenger[x][y] > 0 and not complete[passenger[x][y]]: # 아직 목적지에 못간 손님을 만나면
            # print(passenger[x][y], '손님 만남', x, y, '가는데 사용한 에너지', oil, '남은 에너지', energy-oil)
            candi.append([oil, x, y])

        for i in range(4): # 위 좌 우 하
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not board[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, oil + 1])
        
    return False

ans = True
px, py = 0, 0
for _ in range(M):
    candi = []
    find_passenger()
    if candi:
        candi.sort(key=lambda x:(x[0], x[1], x[2])) # 가장 가깝고 행, 열, 가장 작은 손님
        px, py = candi[0][1], candi[0][2] # 태울 승객 좌표
        energy -= candi[0][0] # 승객 태우러 가면서 사용한 연료 감소
        tx, ty = px, py # 택시 위치 승객 위치로 이동
        
        if not work(px, py):
            ans = False
            break
    else: # 승객 남아있는데 태울 승객을 못찾았으면 -1
        ans = False
        break
    if complete.count(False) == 1:
        break

print(energy if ans else -1)