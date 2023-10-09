di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

n = int(input())
board = [[0]*(n+1) for _ in range(n+1)] # 자리
likes = {} # 학생별 좋아하는 학생들

def check(want):
    result = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] != 0: continue

            count = 0 # 좋아하는 학생이 인접한 수
            count2 = 0 # 인접한 빈 칸 수
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 1 or ni > n or nj < 1 or nj > n:
                    continue
                if board[ni][nj] in want:
                    count += 1
                if board[ni][nj] == 0:
                    count2 += 1
            result.append((count, count2, i, j))
            
    return result

for _ in range(n*n):
    like = list(map(int, input().split()))
    likes[like[0]] = like[1:]
    candi = check(like[1:])
    candi.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]), reverse=True)
    i = candi[0][2]
    j = candi[0][3]
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