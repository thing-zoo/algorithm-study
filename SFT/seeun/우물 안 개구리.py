import sys
n, m = map(int, input().split())
w = [0]+list(map(int, input().split()))
graph = [[] for _ in range(n+1)] # graph[i]: i와 친분이 있는 사람 번호
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

ans = 0
for i in range(1, n+1):
  strong = True
  for node in graph[i]: # 친분이 있는 사람들 중
    if w[i] <= w[node]: # 나보다 센 사람 있으면
      strong = False # 최고라고 생각하지 않음
      break
  if strong:
    ans += 1
print(ans)