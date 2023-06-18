import heapq, sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
jewelry = [list(map(int, input().rstrip().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewelry.sort()
bags.sort()
res = 0
tmp = []
for b in bags: # 가벼운 가방 부터 보석 넣기
    while jewelry and jewelry[0][0] <= b: # 가장 가벼운 보석의 무게가 가방 무게보다 작으면
        heapq.heappush(tmp, -jewelry[0][1]) # 보석의 가치를 최대힙에 저장
        heapq.heappop(jewelry) # 보석은 삭제
    # 넣을 수 있는 보석 중에 가치가 가장 큰 보석을 현재 가방에 넣음
    if tmp:
        res += -1*heapq.heappop(tmp)
    elif not jewelry:
        break
print(res)
