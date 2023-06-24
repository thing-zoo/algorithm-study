import heapq
  
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # 다익스트라를 위한 초기값 설정
    distance = [float('inf')] * (n+1)
    queue = []
    heapq.heappush(queue, [1, 0])
    distance[1] = 0

    # 다익스트라 시작
    while queue:
        node, dist = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for no in graph[node]:
            if distance[no] > dist + 1:
                distance[no] = dist+1
                heapq.heappush(queue, [no, dist+1])

    maxdist = max(distance[1:])
    answer = distance.count(maxdist)
    
    return answer