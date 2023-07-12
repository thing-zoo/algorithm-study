import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
queue = deque()
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    indegree[b] += 1
    graph[a].append(b)

# indegree가 0인 노드 큐에 넣음
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)


while queue:
    stud = queue.popleft()
    print(stud, end=" ") # 줄 세우기
    for i in graph[stud]: # stud에 연결된 노드들의 indegree 1 빼주기
        indegree[i] -= 1 
        if indegree[i] == 0: # 0이면 큐에 넣기
            queue.append(i)