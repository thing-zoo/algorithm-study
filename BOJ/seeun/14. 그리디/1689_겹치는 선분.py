import sys, heapq
input = sys.stdin.readline
n = int(input())
line = [list(map(int, input().rstrip().split())) for _ in range(n)]
line.sort(key=lambda x: x[0])
hq = []
ans = 1
heapq.heappush(hq, line[0][1])
for i in range(1, n):
    while hq and hq[0] <= line[i][0]: # 이전까지의 선분 중 "현재 왼쪽 좌표 이전에 끝나는 선분들 pop"
        heapq.heappop(hq)
    heapq.heappush(hq, line[i][1]) # 현재 선분의 오른쪽 좌표를 넣음
    ans = max(ans, len(hq)) # 현재 겹치는 개수
print(ans)
