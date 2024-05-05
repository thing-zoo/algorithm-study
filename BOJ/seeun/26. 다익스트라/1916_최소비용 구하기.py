import heapq, sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [float('inf')] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())
def dijkstra(x):
    hq = []
    heapq.heappush(hq, [0, x]) # 시작 지점 초기 거리 0, 시작 지점 저장
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for i in graph[node]: # 현재 노드에서 갈 수 있는 노드들 확인
            if distance[i[0]] > dist + i[1]: # 출발 -> 현재 노드 거쳐서 -> i노드
                distance[i[0]] = dist + i[1]
                heapq.heappush(hq, [distance[i[0]], i[0]])

dijkstra(start)
print(distance[end])