from collections import deque

footprint= deque()

n = int(input())
board = [[0]*n for _ in range(n)]
apple_n = int(input())

# 사과가 있는 곳에 9 표시
for _ in range(apple_n):
    x, y = map(int, input().split())
    board[x-1][y-1] = 9

dir_n = int(input())
dir_list = []
for _ in range(dir_n):
    x, d = input().split()
    x = int(x)
    dir_list.append([x, d])

# dir: north-0, east-1, south-2, west-3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
head = [0,0]
tail = [0,0]
dir = 1 # initial dir: east
time = 0
i = 0 # dir 리스트를 위한 인덱스
flag = False # 사과 못먹었을 때 꼬리를 앞으로 당겨주기 위한 변수

while True:
    time += 1
    if [head[0]+dx[dir], head[1]+dy[dir]] in footprint: # 지금 앞으로 갈 곳이 내 몸뚱아리면?
        break
    if flag: # 사과를 못먹었으면 
        tail = footprint.popleft() # 꼬리를 머리가 있었던 곳으로 가져옴
    flag = False

    # 머리 한칸 앞으로 이동
    head[0] += dx[dir]
    head[1] += dy[dir]
    if head[0]<0 or head[0]>=n or tail[0]<0 or  tail[0]>=n or head[1]<0 or head[1]>=n or tail[1]<0 or tail[1]>= n: # 벽에 부딪히면
        break
    # 일단 전진
    footprint.append([head[0], head[1]])
    if board[head[0]][head[1]] != 9: # 머리칸에 사과가 없으면
        flag = True
    else: board[head[0]][head[1]] = 0 # 사과 있으면 먹었으니까  0으로 만들어줌
        
    # 방향 바꿀 시간이 오면 방향 틀어주기
    if i<dir_n and dir_list[i][0] == time:
        if dir_list[i][1] == 'D':
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4
        i+=1

print(time)