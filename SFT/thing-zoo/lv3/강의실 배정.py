import heapq
n = int(input())
times = []
for _ in range(n):
    s, f = map(int, input().split())
    heapq.heappush(times, (f, s)) # 빨리 끝나는 순
end = 0
answer = 0
while times:
    f, s = heapq.heappop(times)
    if end <= s:
        end = f
        answer += 1
print(answer)