import sys, heapq
input = sys.stdin.readline
n = int(input())
meetings = [list(map(int, input().rstrip().split())) for _ in range(n)]
meetings.sort() # 시작시간 기준 오름차순 정렬
answer = 0 # 최소 회의실 개수
ends = [meetings[0][1]] # 끝나는 시간 최소힙
heapq.heapify(ends)
for s, e in meetings[1:]:
    if ends[0] <= s:
        heapq.heappop(ends)
    heapq.heappush(ends, e)
print(len(ends))