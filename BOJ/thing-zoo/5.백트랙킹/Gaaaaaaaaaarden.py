from itertools import combinations
from collections import deque
import copy
def bfs(graph, selected, red):
    count = 0
    red_q = deque()
    green_q = deque()
    for x, y in selected:
        if [x,y] in red:
            red_q.append([x, y])
            graph[x][y] = 3
        else:
            green_q.append([x, y])
            graph[x][y] = 4
    
    while red_q: # 빨간색 배양액이 없어질때까지
        green_temp = set()
        red_temp = set()
        while red_q: # 빨간색 배양액 퍼뜨리기
            x,y = red_q.popleft()
            graph[x][y] = 3
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 or graph[nx][ny] == 2:
                        red_temp.add((nx, ny))
        while green_q: # 초록색 배양액 퍼뜨리기
            x,y = green_q.popleft()
            graph[x][y] = 4
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 or graph[nx][ny] == 2:
                        green_temp.add((nx, ny))

        inter = green_temp & red_temp # 겹치는 영역 => 꽃
        green_temp = green_temp - inter
        red_temp = red_temp - inter

        for x, y in inter:
            graph[x][y] = 5
            count += 1 # 꽃 카운트
        for x, y in red_temp:
            graph[x][y] = 3
        for x, y in green_temp:
            graph[x][y] = 4
        red_q.extend(red_temp)
        green_q.extend(green_temp)

    return count

    
n, m, g, r = map(int, input().split())
maps = []
max_flower = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

candidate = [] # 배양액을 뿌릴 땅의 후보
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j] == 2: # 배양액을 뿌릴 수 있는 땅이면
            candidate.append([i, j])

for selected in combinations(candidate, r+g): # 후보중 r+g개 고른 조합
    for red in combinations(selected, r): # r+g개중 r개만 고른 조합
        copy_maps = copy.deepcopy(maps)
        max_flower = max(max_flower, bfs(copy_maps, selected, red))
print(max_flower)