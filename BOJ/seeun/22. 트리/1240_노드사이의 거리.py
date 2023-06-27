from collections import deque

def bfs(start, end, dist):
    global distance
    queue = deque()
    queue.append([start, 0])

    while queue:
        node, dist = queue.popleft()
        if node == end: # 현재 노드가 찾는 노드이면 지금까지 이동한 거리 리턴
            return dist
        for n in tree[node]:
            if not visited[n[0]]:
                visited[n[0]] = True
                queue.append([n[0], dist+n[1]])

n ,m = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d)) # 노드 사이의 거리를 함께 저장
    tree[b].append((a, d))

for _ in range(m):
    a, b = map(int, input().split())
    visited = [False] * (n+1)
    distance = bfs(a, b, 0) # 시작, 도착, 거리
    print(distance)