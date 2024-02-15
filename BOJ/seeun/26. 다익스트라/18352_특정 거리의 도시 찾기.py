import heapq, sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
distance = [float('inf')] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

hq = []
heapq.heappush(hq, [0, x])
distance[x] = 0
while hq:
    dist, node = heapq.heappop(hq)
    if distance[node] < dist: # x->node까지 거리가dist보다 작으면
        continue # 넘어가기
    for i in graph[node]: # node에 연결된 곳 갱신
        if distance[i] > dist + 1: # node를 거쳐서 i에 가는 것이 지금보다 짧으면
            distance[i] = dist + 1 # 갱신
            heapq.heappush(hq, [dist+1, i]) # i노드 힙에 넣어서 또 확인

if distance.count(k):
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
else:
    print(-1)