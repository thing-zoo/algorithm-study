import sys
input = sys.stdin.readline
n = int(input())
pos = [list(map(int,input().rstrip().split())) for _ in range(n)]
pos.sort()
answer = 0
x, y = pos[0]
for i in range(1, n):
    x2, y2 = pos[i]
    if x <= x2 <= y: # 이전과 겹치면
        y = max(y, y2) # y값 갱신
    else: # 겹치지 않으면
        answer += y - x # 선의 길이 더하고
        x, y = x2, y2 # x, y 갱신
answer += y - x
print(answer)