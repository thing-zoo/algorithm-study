import sys
input = sys.stdin.readline
n = int(input())
meet = [list(map(int, input().rstrip().split())) for _ in range(n)]
meet.sort(key=lambda x:(x[1], x[0])) # 끝나는 시간이 빠른 순서대로 정렬

ans = 0 # 가능한 회의 수
now = 0 # 현재 시각
for i in range(n):
    if meet[i][0] >= now: # 시작시간이 지금 현재 시간이랑 같거나 이후이면
        now = meet[i][1] # 회의진행 -> 현재시각을 회의 끝난 시간으로 변경
        ans += 1

print(ans)