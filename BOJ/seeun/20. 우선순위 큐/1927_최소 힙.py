import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
pq = PriorityQueue()
for _ in range(n):
    x = int(input())
    if x:
        pq.put(x)
    else:
        if pq.empty():
            print(0)
        else:
            print(pq.get())