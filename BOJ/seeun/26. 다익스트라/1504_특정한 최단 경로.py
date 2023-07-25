import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int , input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [float('inf')] * (n+1) # 최댓값으로 초기화
    hq = []
    heapq.heappush(hq, [0, start]) # 시작점 넣어놓기
    distance[start] = 0 # 출발점 값 0으로 설정
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist: # 출발점~현재 노드까지의 거리가 이미 더 작은 값으로 갱신되었다면 검사할 필요 X
            continue
        for i in graph[node]: # 현재 노드를 거쳐서 갈 수 있는 노드들의 distance 갱신
            if distance[i[0]] > dist + i[1]: # 출발점->i노드 vs 출발점->node->i노드 둘 중에 작은 것으로
                distance[i[0]] = dist + i[1]
                heapq.heappush(hq, [distance[i[0]], i[0]]) # 갱신되었으면 여기에 연결된 노드들도 검사해야되기 때문에 힙에 넣기

    return distance

# 시작점이 1
oneto = dijkstra(1)

# 시작점이 v1
v1to = dijkstra(v1)

# 시작점이 v2
v2to = dijkstra(v2)

tmp1 = oneto[v1] + v1to[v2] +v2to[n] # 1->v1->v2->n
tmp2 = oneto[v2] + v2to[v1] +v1to[n] # 1->v2->v1->n

ans = min(tmp1, tmp2)
if ans != float('inf'):
    print(ans)
else:
    print(-1)