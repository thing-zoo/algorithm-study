import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [float('inf')] * (n+1)
hq = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
s, e = map(int, input().split())
route = [[s] for _ in range(n+1)]

heapq.heappush(hq, [0, s])
distance[s] = 0
while hq:
    dist, node = heapq.heappop(hq)
    if dist > distance[node]:
        continue
    for i in graph[node]:
        if distance[i[0]] > dist + i[1]: # node를 거쳐서 오는 것이 더 빠르면
            distance[i[0]] = dist + i[1]
            route[i[0]] = route[node] + [i[0]] # node를 거쳐서 i노드에 오는 루트로 변경해줌
            heapq.heappush(hq, [distance[i[0]], i[0]])

print(distance[e])
print(len(route[e]))
print(*route[e])