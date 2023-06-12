import sys, heapq
input = sys.stdin.readline
n = int(input())
pq = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(pq, -x)
    else:
        if len(pq):
            print(-heapq.heappop(pq))
        else:
            print(0)