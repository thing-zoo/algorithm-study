import sys, heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [float('inf')] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append([a, c]) # 단방향 도로를 반대로 바꿔서 저장 -> 면접장에서 각 도시로의 거리를 측정함
interview = list(map(int, input().split()))
hq = []
for i in interview:
    distance[i] = 0 # 면접장이 있는 도시들은 이동거리 0
    heapq.heappush(hq, [0, i]) # 모든 면접장에서 다익스트라를 시작함

while hq:
    dist, city = heapq.heappop(hq)
    if distance[city] < dist:
        continue
    for c in graph[city]:
        if distance[c[0]] > dist + c[1]:
            distance[c[0]] = dist + c[1]
            heapq.heappush(hq, [distance[c[0]], c[0]])

ansdist = max(distance[1:]) # 최댓값
ans = distance.index(ansdist) # 최댓값인 지역번호
print(ans)
print(ansdist)