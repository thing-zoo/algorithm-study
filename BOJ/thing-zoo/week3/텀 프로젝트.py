from collections import deque
import sys
sys.setrecursionlimit(200000) # 재귀 깊이 초과 예방
input = sys.stdin.readline
def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)
    w = graph[v]
    if visited[w]: # 방문했던 정점
        if w in cycle: # 사이클이 생성되었다면
            result += cycle[cycle.index(w):] # 사이클 넣기
        return
    dfs(w) 
        
for _ in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().rstrip().split()))
    visited = [False]*(n+1)
    result = [] # 팀을 형성한 사람을 담음
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-len(result)) # 팀이 없는 사람 수