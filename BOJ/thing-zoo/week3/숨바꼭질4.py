import sys
from collections import deque
def bfs():
    q = deque([n])
    path[n] = -2 # 시작점 표시 겸 방문 표시
    while q:
        x = q.popleft()
        if x == k:
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and path[nx] == -1: # 방문확인
                path[nx] = x # 경로 저장
                q.append(nx)

input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 10 ** 5
path = [-1]*(MAX+1) # 방문 확인 겸 경로 저장

bfs()
i = path[k]
result = [k]
while i != -2:
    result.append(i)
    i = path[i]
result.reverse()
print(len(result)-1)
print(*result)