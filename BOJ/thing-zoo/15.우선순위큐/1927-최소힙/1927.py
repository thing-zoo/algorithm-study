import heapq
import sys
input = sys.stdin.readline
min_heap = []
heapq.heapify(min_heap)
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(min_heap, x)
    else:
        if min_heap:
            sys.stdout.write('%d\n' %(heapq.heappop(min_heap)))
        else:
            sys.stdout.write('0\n')