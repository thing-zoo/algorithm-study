import sys
input = sys.stdin.readline

n = int(input())
board = [input().strip() for _ in range(n)]

# 머리 위치 알아내기
head = [0,0]
for i in range(n):
    if board[i].count("*") == 1:
        head[0] = i
        head[1] = board[i].index("*")
        break
heart = [head[0]+1, head[1]] # 심장 위치
print(heart[0]+1, heart[1]+1)

info = []
info.append(board[heart[0]][:heart[1]].count("*")) # 왼쪽팔 길이
info.append(board[heart[0]][heart[1]+1:].count("*")) # 오른쪽팔 길이

# 허리 길이
tmp = 0
for i in range(heart[0]+1, n):
    if board[i][heart[1]] == "*":
        tmp += 1
    else:
        break
info.append(tmp)

# 양쪽 다리 길이
left, right = 0, 0
for i in range(heart[0]+info[-1]+1, n):
    if board[i][heart[1]-1] == "_" and board[i][heart[1]+1] == "_": # 둘다 다리 끝났으면 종료
        break
    if board[i][heart[1]-1] == "*":
        left += 1
    if board[i][heart[1]+1] == "*":
        right += 1
info.append(left)
info.append(right)
print(*info)