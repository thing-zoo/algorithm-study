from collections import deque
from copy import deepcopy

queue = deque()
queue2 = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

paint = []
cntRGB = 0
cntRB = 0

def bfsRGB(i, j, color):
    global n, cntRGB, cntRB

    queue.append([i, j])
    paint[i][j] = "."
    while queue:
       
        i, j = queue.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx<0 or nx >=n or ny <0 or ny >= n:
                continue
            if paint[nx][ny] == color:
                paint[nx][ny] = '.'
                queue.append([nx, ny])
                
def bfsRB(i, j, color):
    global n, cntRGB, cntRB

    queue2.append([i, j])
    paint[i][j] = "."
    while queue2:
       
        i, j = queue2.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx<0 or nx >=n or ny <0 or ny >= n:
                continue
            if color == 'R' or color == "G":
                if paint2[nx][ny] == "R" or paint2[nx][ny] == "G":
                    paint2[nx][ny] = '.'
                    queue2.append([nx, ny])
            else:
                if paint2[nx][ny] == color:
                    paint2[nx][ny] = '.'
                    queue2.append([nx, ny])
    return False

n = int(input())

for i in range(n):
    paint.append(list(input()))

paint2 = deepcopy(paint)

for i in range(n):
    for j in range(n):
        if paint[i][j] != '.':
            bfsRGB(i, j, paint[i][j])
            cntRGB += 1
        if paint2[i][j] != '.':
            bfsRB(i, j, paint2[i][j])
            cntRB += 1
print(cntRGB, cntRB)