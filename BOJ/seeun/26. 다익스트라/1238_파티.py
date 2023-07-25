import sys, heapq
INF = float('inf')
input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    distance = [INF] * (n+1) # 최댓값으로 초기화
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

# x에서 모든 지역으로 이동하는 값
xtoi = dijkstra(x)

# i에서 x로 가는 최솟값
itox = [0] * (n+1)
for i in range(1, n+1): # 시작점이 i일때
    itox[i] = dijkstra(i)[x] # 도착지점이 x인 값

ans = 0
for i in range(1, n+1):
    ans = max(ans, itox[i] + xtoi[i])
print(ans)