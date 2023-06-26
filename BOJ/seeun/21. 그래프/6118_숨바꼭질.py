import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append([1,b])
    graph[b].append([1,a])

dist = [float('inf')] * n
def dijkstra(start): # 시작점으로부터 
    queue = []
    heapq.heappush(queue, (0, start)) # 시작 노드는 시작노드와 거리가 0
    dist[start] = 0
    while queue:
        d, n = heapq.heappop(queue) # 출발노드에서 가장 거리가 가까운 노드 가져옴
        if dist[n] < d: # 현재 저장된 거리가 지금보다 작으면 이미 검사한 노드 => 패스
            continue
        # 가져온 노드와 연결된 노드들을 가기위한 최단 거리 계산
        for i in graph[n]:
            if dist[i[1]] > d + i[0]: # 출발에서 노드i 까지 그냥 오는것 VS 출발-현재노드-노드i이렇게 거쳐서 오는것
                dist[i[1]] = d + i[0] # 최솟값 갱신
                heapq.heappush(queue, (d + i[0], i[1])) # 갱신된 값으로 힙에 넣기

dijkstra(0)
# print(dist)
maxnum = max(dist)
print(dist.index(maxnum)+1, maxnum, dist.count(maxnum))