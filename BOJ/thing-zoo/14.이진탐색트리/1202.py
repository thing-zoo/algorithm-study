# 작은가방부터 담을 수 있는 최대가치의 보석을 담는다
import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
jewelry = []   # 보석: 무게, 가치
bag = []       # 가방: 최대무게

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewelry, (m, v)) # 무게기준 최소힙
for _ in range(k):
    bag.append(int(input().rstrip()))
bag.sort() # 가방 무게 오름차순 정렬

result = 0
current_jewelry = []
for c in bag:
    while jewelry and c >= jewelry[0][0]: # 가방에 담을 수 있는 보석찾기
        heapq.heappush(current_jewelry, -heapq.heappop(jewelry)[1]) # 가치기준 최대힙
    if current_jewelry:
        result -= heapq.heappop(current_jewelry)
    elif not jewelry:
        break
print(result)