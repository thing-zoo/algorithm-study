from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def find_fish(x, y):
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    can_eat = []
    queue.append([x, y, 0])
    visited[x][y] = True

    while queue:
        x, y, dist= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                if sea[nx][ny] == 0 or sea[nx][ny] == size: # 그냥 바다거나 아기상어랑 같은 사이즈의 물고기: 그냥 지나감
                    queue.append([nx,ny, dist + 1])
                elif sea[nx][ny] < size: # 사이즈가 작으면 먹을수도 있고 지나갈 수도 있음
                    can_eat.append([nx, ny, dist+1])
                    queue.append([nx,ny, dist + 1])
    return can_eat

# main
n = int(input())
sea = []
for _ in range(n):
    sea.append(list(map(int, input().split())))

fish = []
size = 2 # 초기상태 아기상어 크기
for i in range(n):
    for j in range(n):
        if sea[i][j] in [1, 2, 3, 4, 5, 6]:
            fish.append([i, j])
        if sea[i][j] == 9:
            sea[i][j] = 0 # 바다로 바꿔줌
            baby = [i, j]

ate = 0 # 현재까지 먹은 물고기 수(가 사이즈와 같아지면 크기 +1)
time = 0
while True:
    
    eat_list = []
    eat_list = find_fish(baby[0], baby[1])
    
    if len(eat_list)==0: # 먹을 수 있는 물고기가 없으면 stop
        break
    else:
        eat_list = sorted(eat_list, key=lambda x:(x[2], x[0], x[1])) # 거리, 행 ,열 순서대로 정렬
        eat_x, eat_y = eat_list[0][0], eat_list[0][1]

        ate += 1
        if ate != 0 and ate%size==0: # 자기 사이즈만큼 마릿수를 먹었으면 마릿수 초기화, 사이즈 +1
            size += 1
            ate = 0
        sea[eat_x][eat_y] = 0 # 잡아먹음으로 표시
        baby = [eat_x, eat_y] # 아기상어 위치 이동
    time += eat_list[0][2] # 이 물고기를 먹으러 간 거리만큼 시간 추가

print(time)