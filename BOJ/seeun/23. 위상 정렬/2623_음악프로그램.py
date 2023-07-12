import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
queue = deque()
for _ in range(m):
    order = list(map(int, input().strip().split()))
    for i in range(2, len(order)):
        indegree[order[i]] += 1
        graph[order[i-1]].append(order[i])

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

ans = []
while queue: # 위상정렬 시작
    sing = queue.popleft()
    ans.append(sing)
    for i in graph[sing]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

if len(ans) != n:
    print(0)
else:
    for i in ans:
        print(i)