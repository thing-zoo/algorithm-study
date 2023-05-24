import heapq
import sys
input = sys.stdin.readline
max_heap = []
heapq.heapify(max_heap)
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(max_heap, -x)
    else:
        if max_heap:
            sys.stdout.write('%d\n' %(-heapq.heappop(max_heap)))
        else:
            sys.stdout.write('0\n')