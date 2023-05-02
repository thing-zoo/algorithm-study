import sys
input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().rstrip().split())) for _ in range(n)] # 튜플로 입력 받기

lines.sort(key=lambda x:x[0])
start = lines[0][0]
end = lines[0][1]
ans = 0
for i in range(1,n):
    if lines[i][0] <= end: # 시작점이 현재 라인에 포함
        end = max(lines[i][1], end)
    else:
        ans += end-start
        start, end = lines[i]
    # print(start, end, ans)
ans += end-start
print(ans)