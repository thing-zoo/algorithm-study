from collections import deque
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)] # 양분 로봇
board = [[5]*n for _ in range(n)] # 땅
trees = [[deque() for _ in range(n)] for _ in range(n)] # 살아있는 나무
dead_trees = [[list() for _ in range(n)] for _ in range(n)] # 죽은 나무
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(k): # k년 반복
    # 봄
    for i in range(n):
        for j in range(n):
            size = len(trees[i][j])
            for k in range(size):
                if board[i][j] < trees[i][j][k]: # 나이만큼 양분이 없으면
                    for _ in range(k, size): # 이후 나무들은
                        dead_trees[i][j].append(trees[i][j].pop()) # 죽음
                    break
                else:
                    board[i][j] -= trees[i][j][k] # 나이만큼 양분 먹음
                    trees[i][j][k] += 1 # 나이 증가

    # 여름
    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                board[i][j] += dead_trees[i][j].pop()//2 # 죽은 나무들은 양분이 됨

    # 가을 & 겨울
    for i in range(n):
        for j in range(n):
            size = len(trees[i][j])
            for k in range(size):
                if trees[i][j][k] % 5 != 0: continue  # 5배수만 번식
                for d in range(8): # 인접한 8칸에
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
                    trees[ni][nj].appendleft(1) # 나이가 1인 나무 맨앞에 넣기
            board[i][j] += a[i][j] # 양분 로봇 수행

answer = 0 # k년 후 살아있는 나무 개수
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)