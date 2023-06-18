import sys, heapq
input = sys.stdin.readline
n = int(input())
pq = []

for i in range(n):
    tmp = list(map(int, input().rstrip().split()))
    for j in range(n):
        if len(pq) == n: # 힙의 최대 크기는 n
            if pq[0] < tmp[j]: # 최솟값이 나보다 작다면 
                heapq.heappop(pq) # 삭제 후 삽입
                heapq.heappush(pq, tmp[j])
        else: # 힙의 크기가 n보다 작으면 그냥 삽입
            heapq.heappush(pq, tmp[j]) 

print(heapq.heappop(pq))