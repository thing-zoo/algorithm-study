import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
data = []
for _ in range(n):
    deadline, cup = map(int, input().split())
    data.append((deadline, cup))
data.sort(key=lambda x: (x[0], -x[1])) # 마감시간 오름차순, 컵 개수 내림차순 정렬

q = [] # 최소힙의 크기가 곧 현재 시간!
for deadline, cup in data:
    heapq.heappush(q, cup) # 일단 컵 개수 넣어
    if deadline < len(q): # 현재시간이 마감시간보다 크면
        heapq.heappop(q) # 최소값 삭제
print(sum(q))
