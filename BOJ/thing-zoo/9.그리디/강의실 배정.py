import sys
import heapq
input = sys.stdin.readline
n = int(input())
schedule = [list(map(int, input().rstrip().split())) for _ in range(n)]
schedule.sort() # 시작시간이 빠른순으로 정렬
ends = [schedule[0][1]] # 끝난 시간 배열
heapq.heapify(ends) # 힙을 통해 끝난시간이 빠른순으로 정렬
for i in range(1, n):
    s, t = schedule[i]
    if ends[0] <= s: # 이전 강의중 가장 빨리 끝나는 강의 이후에 시작하면
        heapq.heappop(ends) # 가장 빨리 끝나는 강의는 빼기
    heapq.heappush(ends, t) # 지금 강의의 끝나는 시간 넣기
print(len(ends))