from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
pq = PriorityQueue()
for _ in range(n):
    tmp = int(input())
    pq.put(tmp)

ans = 0
while pq.qsize() >1:
    a = pq.get()
    b = pq.get()
    ans += (a+b)
    pq.put(a+b)
print(ans)