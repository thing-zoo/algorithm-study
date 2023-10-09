di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

n = int(input())
board = [[0]*(n+1) for _ in range(n+1)] # 자리
likes = {} # 학생별 좋아하는 학생들

def check1(want): # 좋아하는 학생이 인접한 칸에 가장 많은 칸들 구하기
    result = []
    max_count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] != 0: continue

            count = 0 # 좋아하는 학생이 인접한 수
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 1 or ni > n or nj < 1 or nj > n:
                    continue
                if board[ni][nj] in want:
                    count += 1
            if max_count < count:
                max_count = count
                result = [[i, j]]
            elif max_count == count:
                result.append([i, j])
    return result

def check2(data): # 인접한 빈 칸이 가장 많은 칸들 구하기
    result = []
    max_count = 0
    for i, j in data:
        count = 0 # 인접한 빈 칸 수
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 1 or ni > n or nj < 1 or nj > n:
                continue
            if board[ni][nj] == 0:
                count += 1
        if max_count < count:
            max_count = count
            result = [[i, j]]
        elif max_count == count:
            result.append([i, j])
    return result

def check3(data): # 행의 번호가 가장 작은 칸들
    result = []
    min_i = n
    for i, j in data:
        if min_i > i:
            min_i = i
            result = [[i, j]]
        elif min_i == i:
            result.append([i, j])
    return result

def check4(data): # 열의 번호가 가장 작은 칸
    result = []
    min_j = n
    for i, j in data:
        if min_j > j:
            min_j = j
            result = [[i, j]]
        elif min_j == j:
            result.append([i, j])
    return result

for _ in range(n*n):
    like = list(map(int, input().split()))
    likes[like[0]] = like[1:]

    candi = check1(like[1:])
    if len(candi) == 1:
        i, j = candi[0][0], candi[0][1]
        board[i][j] = like[0]
        continue

    candi = check2(candi)
    if len(candi) == 1:
        i, j = candi[0][0], candi[0][1]
        board[i][j] = like[0]
        continue

    candi = check3(candi)
    if len(candi) == 1:
        i, j = candi[0][0], candi[0][1]
        board[i][j] = like[0]
        continue

    candi = check4(candi)
    if len(candi) == 1:
        i, j = candi[0][0], candi[0][1]
        board[i][j] = like[0]

answer = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        count = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 1 or ni > n or nj < 1 or nj > n:
                continue
            if board[ni][nj] in likes[board[i][j]]:
                count += 1

        if count == 0:
            continue
        answer += 10 ** (count-1)
print(answer)