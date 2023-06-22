from collections import deque
import sys

def bfs(start):
    queue = deque()
    flag = 1
    queue.append([start, flag])
    while queue:
        node, flag = queue.popleft()
        for n in graph[node]: # 인접한 노드들 검사
            if not visited[n]: # 아직 방문하지 않은 노드이면
                visited[n] = -flag # 현재 노드와 다른 색깔로 칠하고
                queue.append([n, -flag]) # 큐에 넣기
            elif visited[n] ==  visited[node]: # 인접한 노드가 같은 숫자이면 이분그래프 아님
                return False 
    return True


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    v, e = map(int, input().rstrip().split())
    graph = [[]for _ in range(v)]
    visited = [False] * v
    for _ in range(e):
        a, b = map(int, input().rstrip().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
        
    flag = True # 이분그래프인지 아닌지
    for i in range(v): # 모든 노드들에 대해서
        if not visited[i]: # 방문하지 않은 노드이면 탐색
            if bfs(i): # 이분그래프 성공이면 계속
                continue
            else: # 한번이라도 이분그래프가 아닌것이 있으면
                flag = False
                print('NO') # no 출력하고 탐색 종료
                break
    if flag: # 모두 성공했으면
        print('YES')

