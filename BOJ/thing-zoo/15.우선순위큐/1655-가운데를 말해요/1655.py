import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
left_q = []     # 최대힙, 중앙값미만
right_q = []    # 최소힙, 중앙값이상, 루트 = 중앙값
for i in range(1, n+1):
    x = int(input().rstrip())
    if i == 1 or right_q[0] <= x: heapq.heappush(right_q, x)
    else: heapq.heappush(left_q, -x)

    left_size = 0 # left_q의 크기가 되어야할 값
    if i%2 != 0: left_size = i//2
    else: left_size = i//2-1
    
    if len(left_q) > left_size:
        heapq.heappush(right_q, -heapq.heappop(left_q))
    elif len(left_q) < left_size:
        heapq.heappush(left_q, -heapq.heappop(right_q))
    sys.stdout.write("%d\n" %(right_q[0]))