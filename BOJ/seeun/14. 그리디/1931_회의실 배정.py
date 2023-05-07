import sys
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().rstrip().split())))

# 끝나는 시간 -> 시작시간 기준으로 정렬
time.sort(key=lambda x:(x[1], x[0]))
now = 0
cnt = 0
for i in range(n):
    if time[i][0] >= now:
        now = time[i][1]
        cnt += 1
print(cnt)