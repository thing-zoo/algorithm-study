import heapq
import sys
input = sys.stdin.readline
q = []
for _ in range(int(input().rstrip())):
    heapq.heappush(q, int(input().rstrip()))

result = 0
while len(q) > 1:
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    result += x + y
    heapq.heappush(q, x+y)
print(result)