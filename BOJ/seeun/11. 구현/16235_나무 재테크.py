import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())
death = [] # 칸마다 나무 개수
field = [[5 for _ in range(N)] for _ in range(N)] # 처음 밭은 양분 5로 초기화 되어있음
food =[] # 입력 받는 양분 저장
trees = [[deque() for _ in range(N)] for _ in range(N)] # 받 위치마다 덱을 둬서 여러 나무의 나이들을 저장할 수 있음
cnt = M # 나무의 개수 카운트

for _ in range(N):
    food.append(list(map(int, input().rstrip().split())))

for _ in range(M):
    x, y, age = map(int, input().rstrip().split())
    x -=1
    y -=1
    trees[x][y].append(age)

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

# 봄-여름을 동시에 처리
def spring_summer():
    global cnt
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])): # 그 칸에 심겨있는 나무 개수 만큼 반복
                if field[i][j] >= trees[i][j][k]: # 자기 나이이상의 양분이 있으면
                    field[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else: # 양분 없으면 나보다 나이 많은 애들도 다 못먹음 -> 다 죽음
                    # 양분 처리 해줌
                    for _ in range(k, len(trees[i][j])):
                        field[i][j] += trees[i][j].pop()//2
                        cnt -= 1
                    break

# 가을-겨울을 동시에 처리
def autumn_winter():
    global cnt
    for i in range(N):
        for j in range(N):
            length = len(trees[i][j])
            for k in range(length):
                if trees[i][j][k] % 5 == 0:
                    for t in range(8):
                        nx = i + dx[t]
                        ny = j + dy[t]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1) # 나이가 1인 나무 심음
                            cnt += 1
            field[i][j] += food[i][j] # 겨울엔 양분 보충하기


for i in range(K):
    spring_summer()
    autumn_winter()

print(cnt)