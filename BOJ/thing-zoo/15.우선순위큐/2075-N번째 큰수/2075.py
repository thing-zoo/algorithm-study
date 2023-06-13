import heapq
import sys
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    for j in range(n):
        heapq.heappush(q, temp[j])
        if len(q) > n:
            heapq.heappop(q)
print(q[0])