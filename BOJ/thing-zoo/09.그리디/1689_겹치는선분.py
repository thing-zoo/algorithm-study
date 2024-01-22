import sys, heapq
input = sys.stdin.readline

n = int(input())
pos = [tuple(map(int, input().rstrip().split())) for _ in range(n)] # (s, e)
pos.sort() # s기준 오름차순 정렬
answer = 1
min_hq = [pos[0][1]] # e 최소힙 -> 겹친 선분들
for i in range(1, n):
    s, e = pos[i]
    while min_hq and min_hq[0] <= s: # 해당 선분과 안 겹치면
        heapq.heappop(min_hq) # 해당 선분 제거
    heapq.heappush(min_hq, e) # 현재 선분 넣기
    answer = max(answer, len(min_hq)) # 겹친 선분 개수 갱신
print(answer)