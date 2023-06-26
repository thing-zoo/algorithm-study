from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    graph[b].append(a)

def bfs(start):
    queue = deque()
    visited = [False] * n
    visited[start] = True
    cnt = 0 # 현재 노드에서 시작해서 몇개의 노드를 거쳐갈 수 있는지
    queue.append(start)
    while queue:
        node = queue.popleft()
        cnt += 1
        if graph[node]:
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
    return cnt

answer = []
maxnum = 0
for i in range(n):
    tmp = bfs(i)
    if tmp > maxnum: # 현재 값이 최댓값보다 크면
        maxnum = tmp # 최댓값 갱신
        answer = [] # 최댓값 배열 초기화
        answer.append(i+1)
    elif tmp ==  maxnum: # 현재 값이 최댓값과 같으면
        answer.append(i+1) # 최댓값 배열에 추가
print(*answer)