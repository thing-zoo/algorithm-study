import heapq
n, m = map(int, input().split())
a = list(map(int, input().split())) # 카드
heapq.heapify(a) # 최소힙으로 만들기
for _ in range(m): # m번 합체
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    heapq.heappush(a, x+y)
    heapq.heappush(a, x+y)
print(sum(a))