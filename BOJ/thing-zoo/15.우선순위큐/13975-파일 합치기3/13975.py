import heapq
for _ in range(int(input())):
    k = int(input())
    q = list(map(int, input().split()))
    heapq.heapify(q)
    answer = 0
    while len(q) > 1:
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        answer += x + y
        heapq.heappush(q, x + y)
    print(answer)