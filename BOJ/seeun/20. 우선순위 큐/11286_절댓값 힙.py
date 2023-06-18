from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
pq = PriorityQueue()

for i in range(n):
    tmp = int(input())
    if tmp:
        pq.put((abs(tmp), tmp))
    else:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])